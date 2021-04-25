import tkinter as tk
from tkinter.filedialog import askopenfilename

import dungeon_pkmn_randomizer.randomizer as dun_pk_randomizer

window = tk.Tk()

options = {
    "randomize_pokemon"  : {
        "selected" : tk.BooleanVar(),
        "action"   : dun_pk_randomizer.randomize
    },
}

def start(path, status):
    for _, option in options.items():
        if option["selected"].get():
            option["action"](path)
    status.set("DONE!")

window.geometry("400x200")

rom_path = tk.StringVar()
rom_path.set("No file selected...")
rom_path_label = tk.Label(window, textvariable = rom_path)

file_select_btn = tk.Button(window,
                            text = "Select rom to randomize",
                            command = lambda: rom_path.set(askopenfilename()))

check_pokemon = tk.Checkbutton(window,
                               text = "Randomize Pokémon in dungeons",
                               variable = options["randomize_pokemon"]["selected"])

start_btn = tk.Button(window, text = "Start", command = lambda: start(rom_path.get(), status_var))

status_var = tk.StringVar()
status_var.set("")
status_label = tk.Label(window, textvariable = status_var)

rom_path_label.pack()

file_select_btn.pack()

check_pokemon.deselect()
check_pokemon.pack()

start_btn.pack()

status_label.pack()

window.mainloop()
