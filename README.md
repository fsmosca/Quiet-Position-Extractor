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
Analyze wacnew.epd
```
D:\github\Quiet-Position-Extractor>python qpe.py --input "./epd/wacnew.epd" --movetimems 200 --engine "./engine/stockfish-11-win/stockfish_20011801_x64_modern.exe" --engineoption "Hash=128" --log
Analysis starts ...
pos: 1
Skip, score is a mate.
pos: 2
Skip, the bm in 8/7p/5k2/5p2/p1p2P2/Pr1pPK2/1P1R3P/8 b - - bm Rxb2; id "WAC.002"; is tactical.
pos: 3
['e3g3']
Skip, pv length is below 4 plies.
pos: 4
Skip, the bm in r1bq2rk/pp3pbp/2p1p1pQ/7P/3P4/2PB1N2/PP3PPR/2KR4 w - - bm Qxh7+; id "WAC.004"; is tactical.
pos: 5
Skip, the bm in 5k2/6pp/p1qN4/1p1p4/3P4/2PKP2Q/PP3r2/3R4 b - - bm Qc4+; id "WAC.005"; is tactical.
pos: 6
['b6b7']
Skip, pv length is below 4 plies.
pos: 7
saving ...
rnbqkb1r/pppp1ppp/8/4P3/6n1/7P/PPPNPPP1/R1BQKBNR b KQkq - bm Ne3; id "WAC.007";
['Ne3', 'Ngf3', 'Be7', 'a4']
pos: 8
Skip, score is a mate.
pos: 9
Skip, the bm in 3q1rk1/p4pp1/2pb3p/3p4/6Pr/1PNQ4/P1PB1PP1/4RRK1 b - - bm Bh2+; id "WAC.009"; is tactical.
pos: 10
Skip, the bm in 2br2k1/2q3rn/p2NppQ1/2p1P3/Pp5R/4P3/1P3PPP/3R2K1 w - - bm Rxh7; id "WAC.010"; is tactical.
...
```


### Credits
* Python-chess  
https://github.com/niklasf/python-chess
