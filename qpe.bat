set MTMS=200
set EPD="./epd/wacnew.epd"

python qpe.py --input %EPD% --movetimems %MTMS% --engine "./engine/stockfish-11-win/stockfish_20011801_x64_modern.exe" --engineoption "Hash=128"


pause
