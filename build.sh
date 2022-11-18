#!/bin/sh

pyinstaller -n pmdrc-randomizer --onefile --console src/main.py
zip -j "linux.zip" "./dist/pmdrc-randomizer" config.json