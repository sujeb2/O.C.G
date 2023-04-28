@echo off
setlocal

python -m pip install --upgrade pip
pip install --upgrade pyqt5
pip install --upgrade pyinstaller

set "psCommand="(new-object -COM 'Shell.Application')^
.BrowseForFolder(0,'Please choose a Python folder.',0,0).self.path""

for /f "usebackq delims=" %%I in (`powershell %psCommand%`) do set "folder=%%I"

setlocal enabledelayedexpansion
echo Choosed !folder
cd !folder
pyinstaller -w customtag.py
pause