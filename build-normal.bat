@echo off
title ctg builder
echo "[INFO] ctg user dist builder v1.0.0"
echo "[INFO] Updating..."
pip install -r requirements.txt
echo "[INFO] Building..."
pyinstaller customtag.py -w --clean --onedir -n ctg ^
    --add-data="./src/img/preview/preview-text-template.png;./src/img/preview/" ^
    --add-data="./src/icon_normal.png;./src/" ^
    --add-data="./src/icon_normal-resized.png;./src/" ^
    --add-data="./src/icon_edit.png;./src/" ^
    --add-data="./src/img/easter/nobitches.jpg;./src/img/easter/" ^
    --add-data="./src/img/easter/not-end-dream.png;./src/img/easter/" ^
    --add-data="./log/debug-log.log;./log/" ^
    --icon=./src/icon_normal.png
pause
exit