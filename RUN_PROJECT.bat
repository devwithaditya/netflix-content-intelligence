@echo off
echo Starting Netflix Content Intelligence Dashboard...
start http://localhost:8000
python -m http.server 8000
pause
