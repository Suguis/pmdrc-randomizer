import os
import sys
import json
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from randomize import randomize

ORIGINAL_ROM_SIZE = 33554432

def main():
    root = tk.Tk()
    root.withdraw()
    rom_path = filedialog.askopenfilename()
    try:
        size = os.path.getsize(rom_path)
        if size != ORIGINAL_ROM_SIZE:
            raise Exception("The selected file size doesn't match the expected rom file size")
        with open('config.json') as config_json:
            config = json.load(config_json)
        randomize(rom_path, config)
    except Exception as e:
        messagebox.showerror("Error", e)

if __name__ == "__main__":
    main()