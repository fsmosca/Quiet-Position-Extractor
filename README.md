# Quiet Position Extractor
Read EPD file, analyze with engine and save positions that are quiet.

### Needed
Python 3.8 and up  
https://www.python.org/downloads/

### Required module
See requirements.txt  
`pip install -r requirements.txt`

### Command line
See qpe.bat  

```
python qpe.py --input ./epd/wacnew.epd --movetimems 1000 --engine "./engine/stockfish-11-win/stockfish_20011801_x64_modern.exe" --engineoption "Hash=128"
```

### Sample run
Analyze tsc.epd in epd folder
```
python qpe.py --input "./epd/tsc.epd" --movetimems 1000 --engine "./engine/stockfish-11-win/stockfish_20011801_x64_modern.exe" --engineoption "Hash=128" --log
Analysis starts ...
pos: 1
['h7h5', 'b2b3']
Skip, pv length is below 4 plies.
pos: 2
saving ...
r1bk3r/ppp1bpp1/2p5/4Pn1p/8/2N2N1P/PPP2PP1/R1B2RK1 w - - acd 14; ce 45; sm Bf4; EngineMove b3; c0 "Event: Croatia GCT 2019, Site: Zagreb CRO, Date: 2019.07.04, Round: 8.6, WhiteElo: 2779, BlackElo: 2748"; WhitePlayer "Vachier Lagrave,M"; BlackPlayer "Karjakin,Sergey"; LegalMoves 31; AnalyzingEngine "Stockfish 11";
['Bf4', 'Ke8', 'Rad1', 'Be6']
pos: 3
['c8e6', 'f1d1']
Skip, pv length is below 4 plies.
pos: 4
['f1d1', 'd8e8']
Skip, pv length is below 4 plies.
pos: 5
saving ...
r1k4r/ppp1bpp1/2p1b3/4Pn1p/5B2/2N2N1P/PPP2PP1/3R1RK1 w - - acd 14; ce 84; sm a3; EngineMove Ng5; c0 "Event: Croatia GCT 2019, Site: Zagreb CRO, Date: 2019.07.04, Round: 8.6, WhiteElo: 2779, BlackElo: 2748"; WhitePlayer "Vachier Lagrave,M"; BlackPlayer "Karjakin,Sergey"; LegalMoves 40; AnalyzingEngine "Stockfish 11";
['Ne4', 'a5', 'a4', 'b6']
pos: 6
['b6', 'Bg5', 'Kb7', 'Bxe7']
Skip, move in the pv has a promote or check or capture move.
pos: 7
['Bg5', 'Kb7', 'Bxe7']
Skip, move in the pv has a promote or check or capture move.
pos: 8
['c8b7']
Skip, pv length is below 4 plies.
pos: 9
['g5e7', 'e8e7']
Skip, pv length is below 4 plies.
pos: 10
Skip, abs score difference between static and search score is above 100 score margin.
static scorecp: -425, search scorecp: 44, abs(44 - (-425)): 469
...
```

### Help
```
(venv) PS D:\github\Quiet-Position-Extractor> python qpe.py --help                                                      usage: QPE - Quiet Position Extractor v0.9.beta [-h] --input INPUT [--outputepd OUTPUTEPD] --engine ENGINE
                                                [--engineoption ENGINEOPTION] [--movetimems MOVETIMEMS]
                                                [--pvlen PVLEN] [--score-margincp SCORE_MARGINCP] [--log]
                                                [--static-eval]

Analyze epd and save quiet positions.

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT         input epd file
  --outputepd OUTPUTEPD
                        output epd file in append mode, default=out.epd
  --engine ENGINE       input engine file
  --engineoption ENGINEOPTION
                        input engine options, e.g --engineoption "Threads=1, Hash=128, Debug Log File=log.txt"
  --movetimems MOVETIMEMS
                        input analysis time in ms, default=1000
  --pvlen PVLEN         input pv length to check moves, default=4
  --score-margincp SCORE_MARGINCP
                        input score margin in cp (centipawn) for the score delta of static eval and search score. If
                        delta is above score margin, the position will not be saved. Default=100
  --log                 a flag to enable logging
  --static-eval         a flag to enable the use of static eval in extracting quiet positions

QPE - Quiet Position Extractor v0.9.beta
```


### Credits
* Python-chess  
https://github.com/niklasf/python-chess
