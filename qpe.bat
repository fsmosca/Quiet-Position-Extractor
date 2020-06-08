set MTMS=1500
set EPD="./epd/wacnew.epd"

:: python qpe.py --input %EPD% --movetimems %MTMS% --engine "./engine/stockfish-11-win/stockfish_20011801_x64_modern.exe" --engine-option "Hash=128"

:: Use static eval
python qpe.py --input %EPD% --movetimems %MTMS% --engine "./engine/stockfish-11-win/stockfish_20011801_x64_modern.exe" --engine-option "Hash=128" --static-eval


pause
