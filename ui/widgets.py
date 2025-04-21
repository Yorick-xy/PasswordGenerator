### ui/widgets.py
import tkinter as tk
from config.theme import BG_COLOR, FG_COLOR, BTN_COLOR, ENTRY_BG, FR_COLOR_BTN

def create_label(root, text, font=("Arial", 11)):
    return tk.Label(root, text=text, bg=BG_COLOR, fg=FG_COLOR, font=font)

def create_entry(root, text_var):
    return tk.Entry(root, textvariable=text_var, font=("Arial", 12), bg=ENTRY_BG, fg=FG_COLOR, insertbackground=FG_COLOR)

def create_button(root, text, command, bg=BTN_COLOR, fg=FR_COLOR_BTN):
    return tk.Button(root, text=text, command=command, font=("Arial", 12), bg=bg, fg=fg, activebackground=bg, activeforeground=fg)

def create_checkbutton(root, text, variable):
    return tk.Checkbutton(root, text=text, variable=variable, bg=BG_COLOR, fg=FG_COLOR, selectcolor=BG_COLOR, font=("Arial", 11))