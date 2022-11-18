import os
import sys
import json
import traceback
from randomize import randomize

from gui import Gui

ORIGINAL_ROM_SIZE = 33554432

def main():
    gui = Gui()
    rom_path = gui.ask_file()

    if rom_path:
        try:
            if os.path.getsize(rom_path) != ORIGINAL_ROM_SIZE:
                raise Exception("The selected file size doesn't match the expected rom file size")

            with open(rom_path, 'rb') as rom_in:
                ba_rom = bytearray(rom_in.read())
            
            randomize(ba_rom)
            generated_rom_path = gui.save_file()
            
            with open(generated_rom_path, 'wb') as rom_out:
                rom_out.write(ba_rom)
        except Exception as e:
            traceback.print_exc()
            gui.show_error(e)

if __name__ == "__main__":
    main()