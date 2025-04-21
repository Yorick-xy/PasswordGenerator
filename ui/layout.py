### ui/layout.py
import tkinter as tk
from tkinter import StringVar, BooleanVar, IntVar
from core.password_logic import generate_password
from core.strength_evaluator import evaluate_strength
from utils.clipboard import copy_to_clipboard
from config.theme import BG_COLOR, ENTRY_BG, HIGHLIGHT_COLOR, FR_COLOR_BTN
from ui.widgets import create_label, create_entry, create_button, create_checkbutton

def build_interface(root):
    length_var = StringVar(value='12')
    digits_var = BooleanVar(value=True)
    special_var = BooleanVar(value=True)
    password_var = StringVar()
    strength_var = IntVar()

    create_label(root, "Longueur du mot de passe :", font=("Arial", 12)).pack(pady=8)
    create_entry(root, length_var).pack()

    create_checkbutton(root, "Inclure des chiffres", digits_var).pack(pady=4)
    create_checkbutton(root, "Inclure des caractères spéciaux", special_var).pack(pady=4)

    def on_generate():
        try:
            length = int(length_var.get())
            pw = generate_password(length, digits_var.get(), special_var.get())
            password_var.set(pw)
            update_strength_bar(pw)
        except ValueError:
            from tkinter import messagebox
            messagebox.showerror("Erreur", "Longueur invalide.")

    def update_strength_bar(password):
        score, label, color = evaluate_strength(password)
        strength_var.set(score)
        strength_bar.config(bg=color, width=int(score * 2))
        strength_label.config(text=label, fg=color)

    create_button(root, "Générer", on_generate).pack(pady=12)
    tk.Entry(root, textvariable=password_var, font=("Courier", 14), width=30, justify='center', state='readonly', bg=ENTRY_BG, fg=HIGHLIGHT_COLOR, readonlybackground=ENTRY_BG).pack(pady=10)
    create_button(root, "Copier", lambda: copy_to_clipboard(password_var.get()), bg="#007acc", fg="white").pack(pady=5)

    create_label(root, "Force du mot de passe :").pack(pady=(10, 2))
    bar_frame = tk.Frame(root, bg=BG_COLOR)
    bar_frame.pack(pady=2)
    global strength_bar, strength_label
    strength_bar = tk.Frame(bar_frame, bg="grey", height=10, width=200)
    strength_bar.pack(side="left")
    strength_label = tk.Label(bar_frame, text="⏳", bg=BG_COLOR, fg="white", font=("Arial", 11), padx=10)
    strength_label.pack(side="left")