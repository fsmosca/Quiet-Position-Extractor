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
python qpe.py --input "./epd/wacnew.epd" --movetimems 1500 --engine "./engine/stockfish-11-win/stockfish_20011801_x64_modern.exe" --engineoption "Hash=128" --static-eval
Analysis starts ...
pos: 1
score: #+2
Skip, score is a mate.
pos: 2
Skip, the bm in 8/7p/5k2/5p2/p1p2P2/Pr1pPK2/1P1R3P/8 b - - bm Rxb2; id "WAC.002"; is tactical.
pos: 3
static scorecp: -38, search scorecp: 598, abs(598 - (-38)): 636
Skip, abs score difference between static and search score is above 100 score margin.
pos: 4
Skip, the bm in r1bq2rk/pp3pbp/2p1p1pQ/7P/3P4/2PB1N2/PP3PPR/2KR4 w - - bm Qxh7+; id "WAC.004"; is tactical.
pos: 5
Skip, the bm in 5k2/6pp/p1qN4/1p1p4/3P4/2PKP2Q/PP3r2/3R4 b - - bm Qc4+; id "WAC.005"; is tactical.
pos: 6
score: #+12
Skip, score is a mate.
pos: 7
static scorecp: -169, search scorecp: 814, abs(814 - (-169)): 983
Skip, abs score difference between static and search score is above 100 score margin.
pos: 8
score: #+7
Skip, score is a mate.
pos: 9
Skip, the bm in 3q1rk1/p4pp1/2pb3p/3p4/6Pr/1PNQ4/P1PB1PP1/4RRK1 b - - bm Bh2+; id "WAC.009"; is tactical.
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
