"""
qpe.py

QPE - Quiet Position Extractor

Analyze EPD and extract those that are quiet.

Requirements:
    Python-chess==0.31.2
"""


import subprocess
import time
from pathlib import Path
import argparse
import logging

import chess
import chess.pgn
import chess.engine


APP_NAME = 'QPE - Quiet Position Extractor'
APP_VERSION = 'v0.8.beta'


def get_time_h_mm_ss_ms(time_delta_ns):
    time_delta_ms = time_delta_ns // 1000000
    s, ms = divmod(time_delta_ms, 1000)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)

    return '{:01d}h:{:02d}m:{:02d}s:{:03d}ms'.format(h, m, s, ms)


def stockfish_staticeval(engineprocess, board):
    """
    command: eval
    result: Total evaluation: 0.13 (white side)
    """
    staticscorecp = None

    fen = board.fen()

    engineprocess.stdin.write('ucinewgame\n')
    engineprocess.stdin.write(f'position fen {fen}\n')

    engineprocess.stdin.write('eval\n')
    for lines in iter(engineprocess.stdout.readline, ''):
        line = lines.strip()
        if 'total evaluation' in line.lower():
            scoreline = line.split('Total evaluation:')[1].strip()
            score = float(scoreline.split('(')[0].strip())
            staticscorecp = int(100*score)
            break

    if staticscorecp is None:
        return None

    return staticscorecp if board.turn else -staticscorecp


def tactical_move(board, epdinfo):
    """
    Tactical move: capture or check or promote or mate.
    """
    if 'bm' not in epdinfo:
        return False

    sanbm = [board.san(m) for m in epdinfo['bm']]
    for m in sanbm:
        if 'x' in m or '+' in m or '=' in m or '#' in m:
            return True

    return False


def runengine(engine_file, engineoption, epdfile, movetimems,
              outputepd, pvlen, scoremargin):
    pos_num = 0
    folder = Path(engine_file).parents[0]
    engine = chess.engine.SimpleEngine.popen_uci(engine_file, cwd=folder)

    # Set engine option
    if engineoption is not None:
        for opt in engineoption.split(','):
            optname = opt.split('=')[0].strip()
            optvalue = opt.split('=')[1].strip()
            engine.configure({optname: optvalue})

    limit = chess.engine.Limit(time=movetimems/1000)
    engineprocess = subprocess.Popen(engine_file, stdin=subprocess.PIPE,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT,
                                     universal_newlines=True, bufsize=1)

    # Open epd file to get epd lines, analyze, and save it.
    with open(epdfile) as f:
        for lines in f:
            ismate, ispromote, ischeck, iscapture = False, False, False, False

            epdline = lines.strip()
            logging.info(epdline)
            board, epdinfo = chess.Board().from_epd(epdline)
            pos_num += 1

            print(f'pos: {pos_num}')

            # Skip if side to move is in check.
            if board.is_attacked_by(not board.turn, board.king(board.turn)):
                print(f'Skip, the side to move is incheck in {epdline}.')
                continue

            # Skip if EPD bm is a tactical move.
            if tactical_move(board, epdinfo):
                print(f'Skip, the bm in {epdline} is tactical.')
                continue

            pv, score = '', None
            with engine.analysis(board, limit) as analysis:
                for info in analysis:
                    if ('upperbound' not in info
                            and 'lowerbound' not in info
                            and 'score' in info
                            and 'pv' in info):
                        pv = info['pv']

                        if info['score'].is_mate():
                            ismate = True

                        score = info['score'].relative.score(mate_score=32000)

            # Don't extract if score is mate or mated
            if ismate:
                print('Skip, score is a mate.')
                continue

            # Compare Stockfish static eval and search score.
            if score is not None and 'stockfish' in engine.id['name'].lower():
                staticeval = stockfish_staticeval(engineprocess, board)
                absdiff = abs(score - staticeval)
                if absdiff > scoremargin:
                    print('Skip, abs score difference between static and '
                          f'search score is above {scoremargin} score margin.')
                    print(f'static scorecp: {staticeval}, '
                          f'search scorecp: {score}, '
                          f'abs({score} - ({staticeval})): {absdiff}')
                    continue

            # Don't extract if there is capture or promote, or a check
            # move in the first pvlen plies of the pv

            # Skip if required pvlen is not meet.
            if len(pv) < pvlen:
                ucipv = [str(m) for m in pv]
                print(ucipv)
                print(f'Skip, pv length is below {pvlen} plies.')
                continue

            # Evaluate pv
            sanpv = []
            for i, m in enumerate(pv):
                if i > pvlen - 1:
                    break

                sanmove = board.san(m)
                sanpv.append(sanmove)

                if len(str(m)) >= 5:
                    ispromote = True
                    break

                if '+' in sanmove:
                    ischeck = True
                    break

                if 'x' in sanmove:
                    iscapture = True
                    break

                board.push(m)

            if ispromote or ischeck or iscapture:
                print(sanpv)
                print('Skip, move in the pv has a promote or check'
                      ' or capture move.')
                continue

            print('saving ...')
            print(epdline)
            print(sanpv)
            with open(outputepd, 'a') as s:
                s.write(f'{epdline}\n')

    engine.quit()

    engineprocess.stdin.write('quit\n')
    print('quit engineprocess')


def main():
    parser = argparse.ArgumentParser(
        prog='%s %s' % (APP_NAME, APP_VERSION),
        description='Analyze epd and save quiet positions.',
        epilog='%(prog)s')
    parser.add_argument('--input', required=True, help='input epd file')
    parser.add_argument('--outputepd', required=False,
                        help='output epd file in append mode, default=out.epd',
                        default='out.epd')
    parser.add_argument('--engine', required=True, help='input engine file')
    parser.add_argument(
        '--engineoption', required=False,
        help='input engine options, e.g '
             '--engineoption "Threads=1, Hash=128, Debug Log File=log.txt"')
    parser.add_argument('--movetimems', required=False, type=int,
                        help='input analysis time in ms, default=1000',
                        default=1000)
    parser.add_argument('--pvlen', required=False, type=int,
                        help='input pv length to check moves, default=4',
                        default=4)
    parser.add_argument('--score-margincp', required=False, type=int,
                        help='input score margin in cp (centipawn) for the '
                             'score delta of static eval and search score. '
                             'If delta is above score margin, the position '
                             'will not be saved. Default=100',
                        default=100)
    parser.add_argument('--log', action="store_true",
                        help='a flag to enable logging')

    args = parser.parse_args()
    epd_file = args.input
    engine_file = args.engine
    outepd_file = args.outputepd
    movetimems = args.movetimems

    # Delete existing epdoutput file
    tmpfn = Path(outepd_file)
    tmpfn.unlink(missing_ok=True)

    if args.log:
        logging.basicConfig(
            level=logging.DEBUG,
            filename='log_quietopeningextractor.txt',
            filemode='w')

    timestart = time.perf_counter_ns()

    print('Analysis starts ...')
    runengine(engine_file, args.engineoption, epd_file, movetimems,
              outepd_file, args.pvlen, args.score_margincp)
    print('Analysis done!')

    elapse = time.perf_counter_ns() - timestart
    print(f'Elapse: {get_time_h_mm_ss_ms(elapse)}')


if __name__ == '__main__':
    main()
