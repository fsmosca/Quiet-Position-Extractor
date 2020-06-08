set MTMS=1500
set EPD="./epd/wacnew.epd"

:: python qpe.py --input %EPD% --movetimems %MTMS% --engine "./engine/stockfish-11-win/stockfish_20011801_x64_modern.exe" --engine-option "Hash=128"

:: Use static eval
:: python qpe.py --input %EPD% --movetimems %MTMS% --engine "./engine/stockfish-11-win/stockfish_20011801_x64_modern.exe" --engine-option "Hash=128" --static-eval

:: Lc0 blas on CPU
python qpe.py --input %EPD% --movetimems %MTMS% --engine "./engine/lc0-v0.25.1-windows-cpu-openblas/lc0.exe" --engine-option "MinibatchSize=8, MaxPrefetch=0" --static-eval


pause
