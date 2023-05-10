@echo off
title ctg builder
echo "[INFO] ctg debug builder v1.0.0"
echo "[INFO] Updating..."
pip install -r requirements.txt
echo "[INFO] Building..."
pyinstaller customtag.py --clean -n ctg --add-data="./src/img/preview/preview-text-template.png;./src/img/preview/" --add-data="./src/icon_normal.png;./src/" --add-data="./log/debug-log.log;./log/" --add-data="./src/icon_normal-resized.png;./src/" --add-data="./src/icon_edit.png;./src" --icon=./src/icon_normal.png
pause