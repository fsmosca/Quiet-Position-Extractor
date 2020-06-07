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
(venv) PS D:\github\Quiet-Position-Extractor> ./qpe.bat                                                                 
D:\github\Quiet-Position-Extractor>set MTMS=200

D:\github\Quiet-Position-Extractor>set EPD="./epd/wacnew.epd"

D:\github\Quiet-Position-Extractor>python qpe.py --input "./epd/wacnew.epd" --movetimems 200 --engine "./engine/stockfish-11-win/stockfish_20011801_x64_modern.exe" --engineoption "Hash=128"
Analysis starts ...
pos: 1
Skip, score is a mate.
pos: 2
[Move.from_uci('b3b8')]
Skip, pv length is below 4 plies.
pos: 3
['Rg3', 'Bg4', 'Rxg4']
Skip, move in the pv has a promote or check or capture move.
pos: 4
Skip, score is a mate.
pos: 5
Skip, score is a mate.
pos: 6
['Rb7', 'Rb5', 'Rxb5']
Skip, move in the pv has a promote or check or capture move.
pos: 7
['Ne3', 'Ngf3', 'Nxd1']
Skip, move in the pv has a promote or check or capture move.
pos: 8
[Move.from_uci('e7f7')]
Skip, pv length is below 4 plies.
pos: 9
Skip, score is a mate.
pos: 10
['Rxh7']
Skip, move in the pv has a promote or check or capture move.
pos: 11
['Bxc6']
Skip, move in the pv has a promote or check or capture move.
pos: 12
Skip, score is a mate.
pos: 13
['Qxf8+']
Skip, move in the pv has a promote or check or capture move.
pos: 14
Skip, score is a mate.
pos: 15
[Move.from_uci('b8b7')]
Skip, pv length is below 4 plies.
pos: 16
['Nc3', 'Qd7', 'Bxc5']
Skip, move in the pv has a promote or check or capture move.
pos: 17
saving ...
1k5r/pppbn1pp/4q1r1/1P3p2/2NPp3/1QP5/P4PPP/R1B1R1K1 w - - bm Ne5; id "WAC.017";
['Ne5', 'Rf6', 'Bg5', 'Be8']
pos: 18
['Rh8', 'Ra1+']
Skip, move in the pv has a promote or check or capture move.
pos: 19
['c6', 'Qxb5']
Skip, move in the pv has a promote or check or capture move.
pos: 20
['Bb5', 'Qxb5+']
Skip, move in the pv has a promote or check or capture move.
pos: 21
['Qh6', 'Qxe1+']
Skip, move in the pv has a promote or check or capture move.
pos: 22
[Move.from_uci('g5f7')]
Skip, pv length is below 4 plies.
pos: 23
[Move.from_uci('g2g4')]
Skip, pv length is below 4 plies.
pos: 24
[Move.from_uci('g7d4')]
Skip, pv length is below 4 plies.
pos: 25
[Move.from_uci('g4h4')]
Skip, pv length is below 4 plies.
pos: 26
[Move.from_uci('d7f5')]
Skip, pv length is below 4 plies.
pos: 27
Skip, score is a mate.
pos: 28
['Qe1+']
Skip, move in the pv has a promote or check or capture move.
pos: 29
['c6', 'bxc6']
Skip, move in the pv has a promote or check or capture move.
pos: 30
['Nxd6']
Skip, move in the pv has a promote or check or capture move.
pos: 31
[Move.from_uci('g2g3')]
Skip, pv length is below 4 plies.
pos: 32
['Qd8+']
Skip, move in the pv has a promote or check or capture move.
pos: 33
['Qe5+']
Skip, move in the pv has a promote or check or capture move.
pos: 34
[Move.from_uci('d4g1')]
Skip, pv length is below 4 plies.
pos: 35
Skip, score is a mate.
pos: 36
[Move.from_uci('e7e1')]
Skip, pv length is below 4 plies.
pos: 37
[Move.from_uci('c6d4'), Move.from_uci('b3d4')]
Skip, pv length is below 4 plies.
pos: 38
['Rd8+']
Skip, move in the pv has a promote or check or capture move.
pos: 39
['Na4', 'Qxa1']
Skip, move in the pv has a promote or check or capture move.
pos: 40
['Rc8', 'a4', 'Rxc4']
Skip, move in the pv has a promote or check or capture move.
pos: 41
Skip, score is a mate.
pos: 42
[Move.from_uci('b4a5'), Move.from_uci('g7f8')]
Skip, pv length is below 4 plies.
pos: 43
[Move.from_uci('a3e7')]
Skip, pv length is below 4 plies.
pos: 44
['dxc4']
Skip, move in the pv has a promote or check or capture move.
pos: 45
['Qxa1']
Skip, move in the pv has a promote or check or capture move.
pos: 46
[Move.from_uci('c3b5'), Move.from_uci('d7f6')]
Skip, pv length is below 4 plies.
pos: 47
[Move.from_uci('c6d4')]
Skip, pv length is below 4 plies.
pos: 48
[Move.from_uci('b8b4'), Move.from_uci('c4f7')]
Skip, pv length is below 4 plies.
pos: 49
[Move.from_uci('h5h6'), Move.from_uci('b2f2')]
Skip, pv length is below 4 plies.
pos: 50
Skip, score is a mate.
...
```


### Credits
* Python-chess  
https://github.com/niklasf/python-chess
