#!/bin/bash
. venv/bin/activate

pyinstaller calculator.py \
    --noconfirm --log-level=WARN \
    --distpath ../dist \
    --workpath ../build \
    --add-data='calculator.ui:.' \
    --icon='icon.png' \
    --upx-dir=/usr/local/share/ \

deactivate
