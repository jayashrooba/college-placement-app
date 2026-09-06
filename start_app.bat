@echo off
cd /d "%~dp0"
start /B pythonw app.py
timeout /t 7 /nobreak >nul
start "" http://127.0.0.1:5000
exit