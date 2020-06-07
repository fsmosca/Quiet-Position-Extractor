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


### Credits
* Python-chess  
https://github.com/niklasf/python-chess
