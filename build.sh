#!/bin/sh

pyinstaller -n pmdrc-randomizer --onefile --console main.py
mkdir -p "release/$OSTYPE"
zip -j "$OSTYPE.zip" "./dist/pmdrc-randomizer" config.json