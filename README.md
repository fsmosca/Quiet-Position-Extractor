# Quiet Position Extractor
Read EPD file, analyze with engine and save positions that are quiet. If the bm in EPD is a capture or a promotion or a check then don't save it. If the side to move is in check, don't save such position too. If those passes the filter, analysis engine is run and check the first 4 or so moves in the pv. If any of the moves in that pv is a capture or promote or a check move then don't save the position as well. Yet another filter is comparing the static score of Stockfish and its search score, if the difference in static score and search score is too much that is above scorecp-margin then don't save such position too.

### Needed
Python 3.8 and up  
https://www.python.org/downloads/

### Required module
See requirements.txt  
`pip install -r requirements.txt`

### Command line
See also qpe.bat  

```
python qpe.py --input ./epd/wacnew.epd --movetimems 1000 --engine "./engine/stockfish-11-win/stockfish_20011801_x64_modern.exe" --engine-option "Hash=128"
```

### Cancel and Continue
* You can cancel current analysis session and continue later. All epds that were already evaluated are saved in evaluated.epd. Make sure the same command line is used as this program will only detect the epd, not the engine, movetime etc. If you have a new command line to run, make sure to delete the evaluated.epd first.  

```
D:\github\Quiet-Position-Extractor>python qpe.py --log --input "./epd/wacnew.epd" --movetimems 1000 --engine "./engine/stockfish-11-win/stockfish_20011801_x64_modern.exe" --engine-option "Hash=128" --static-eval
Analysis starts ...
pos: 1
score: #+2
Skip, score is a mate.
pos: 2
Skip, the bm in 8/7p/5k2/5p2/p1p2P2/Pr1pPK2/1P1R3P/8 b - - bm Rxb2; id "WAC.002"; is tactical.
pos: 3
static scorecp: -38, search scorecp: 588, abs(588 - (-38)): 626
Skip, abs score difference between static and search score is above 100 score margin.
pos: 4
Skip, the bm in r1bq2rk/pp3pbp/2p1p1pQ/7P/3P4/2PB1N2/PP3PPR/2KR4 w - - bm Qxh7+; id "WAC.004"; is tactical.
pos: 5
Skip, the bm in 5k2/6pp/p1qN4/1p1p4/3P4/2PKP2Q/PP3r2/3R4 b - - bm Qc4+; id "WAC.005"; is tactical.
pos: 6
^CTerminate batch job (Y/N)? y
(venv) PS D:\github\Quiet-Position-Extractor> ./qpe.bat                                                                 
D:\github\Quiet-Position-Extractor>set MTMS=1000

D:\github\Quiet-Position-Extractor>set EPD="./epd/wacnew.epd"

D:\github\Quiet-Position-Extractor>python qpe.py --log --input "./epd/wacnew.epd" --movetimems 1000 --engine "./engine/stockfish-11-win/stockfish_20011801_x64_modern.exe" --engine-option "Hash=128" --static-eval
Analysis starts ...
pos: 1
This epd 2rr3k/pp3pp1/1nnqbN1p/3pN3/2pP4/2P3Q1/PPB4P/R4RK1 w - - bm Qg6; id "WAC.001"; is already evaluated.
pos: 2
This epd 8/7p/5k2/5p2/p1p2P2/Pr1pPK2/1P1R3P/8 b - - bm Rxb2; id "WAC.002"; is already evaluated.
pos: 3
This epd 5rk1/1ppb3p/p1pb4/6q1/3P1p1r/2P1R2P/PP1BQ1P1/5RKN w - - bm Rg3; id "WAC.003"; is already evaluated.
pos: 4
This epd r1bq2rk/pp3pbp/2p1p1pQ/7P/3P4/2PB1N2/PP3PPR/2KR4 w - - bm Qxh7+; id "WAC.004"; is already evaluated.
pos: 5
This epd 5k2/6pp/p1qN4/1p1p4/3P4/2PKP2Q/PP3r2/3R4 b - - bm Qc4+; id "WAC.005"; is already evaluated.
pos: 6
score: #+12
Skip, score is a mate.
pos: 7
static scorecp: -169, search scorecp: 816, abs(816 - (-169)): 985
Skip, abs score difference between static and search score is above 100 score margin.
pos: 8
^CTerminate batch job (Y/N)? y
...
```


### Sample run
```
python qpe.py --input "./epd/wacnew.epd" --movetimems 1500 --engine "./engine/stockfish-11-win/stockfish_20011801_x64_modern.exe" --engine-option "Hash=128" --static-eval
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
python qpe.py --help                                                                      
usage: QPE - Quiet Position Extractor v0.16.beta [-h] --input INPUT [--outputepd OUTPUTEPD] --engine ENGINE
                                                 [--engine-option ENGINE_OPTION] [--movetimems MOVETIMEMS] [--pvlen PVLEN]
                                                 [--scorecp-margin SCORECP_MARGIN] [--log] [--static-eval]

Analyze epd and save quiet positions.

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT         input epd file
  --outputepd OUTPUTEPD
                        output epd file in append mode, default=out.epd
  --engine ENGINE       input engine file
  --engine-option ENGINE_OPTION
                        input engine options, e.g --engine-option "Threads=1, Hash=128, Debug Log File=log.txt"
  --movetimems MOVETIMEMS
                        input analysis time in ms, default=1000
  --pvlen PVLEN         input pv length to check moves, default=4
  --scorecp-margin SCORECP_MARGIN
                        input score margin in cp (centipawn) for the score delta of static eval and search score. If delta is
                        above score margin, the position will not be saved. Default=100
  --log                 a flag to enable logging
  --static-eval         a flag to enable the use of static eval in extracting quiet positions

QPE - Quiet Position Extractor v0.16.beta
```


### Credits
* Python-chess  
https://github.com/niklasf/python-chess
