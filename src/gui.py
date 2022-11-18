import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class Gui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()

    def ask_file(self):
        return tk.filedialog.askopenfilename(filetypes=[("Game Boy Advance ROM file", "*.gba"), ("All files", "*")])

    def save_file(self, ):
        return tk.filedialog.asksaveasfile(
            defaultextension=".gba",
            filetypes=[("Game Boy Advance ROM file", "*.gba")]).name

    def show_error(self, e):
        messagebox.showerror("Error", e)