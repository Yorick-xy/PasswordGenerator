# auteur: Yorick MAPET
# date: 10-04-2024

import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip  # pip install pyperclip

def evaluate_strength(pw):
    score = 0
    if len(pw) >= 12:
        score += 40
    elif len(pw) >= 8:
        score += 20
    elif len(pw) >= 5:
        score += 10

    if any(c.islower() for c in pw) and any(c.isupper() for c in pw):
        score += 15
    if any(c.isdigit() for c in pw):
        score += 15
    if any(c in string.punctuation for c in pw):
        score += 20

    return min(score, 100)

def update_strength_bar(pw):
    score = evaluate_strength(pw)
    strength_var.set(score)

    # Couleur & label selon le score
    if score < 30:
        strength_color = "red"
        label_text = "Faible"
    elif score < 60:
        strength_color = "orange"
        label_text = "Moyen"
    elif score < 85:
        strength_color = "yellow"
        label_text = "Bon"
    else:
        strength_color = "lime"
        label_text = "Fort"

    strength_bar.config(bg=strength_color, width=int(score * 2))
    strength_label.config(text=label_text, fg=strength_color)

def generate_password():
    try:
        length = int(length_var.get())
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un nombre valide pour la longueur.")
        return

    if length < 4:
        messagebox.showwarning("Erreur", "La longueur doit être au moins de 4.")
        return

    characters = string.ascii_letters
    if digits_var.get():
        characters += string.digits
    if special_var.get():
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("Erreur", "Aucun jeu de caractères sélectionné.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)
    update_strength_bar(password)

def copy_to_clipboard():
    password = password_var.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copié", "Mot de passe copié dans le presse-papiers !")
    else:
        messagebox.showwarning("Vide", "Aucun mot de passe à copier.")

# Thème sombre
BG_COLOR = "#1e1e1e"
FG_COLOR = "#ffffff"
FR_COLOR_BTN = "#000000"
BTN_COLOR = "#3c3f41"
ENTRY_BG = "#2d2d2d"

# Fenêtre principale
root = tk.Tk()
root.title("🔐 Générateur de mot de passe sécurisé")
root.geometry("420x420")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# Variables
length_var = tk.StringVar(value='12')
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)
password_var = tk.StringVar()
strength_var = tk.IntVar()

# Widgets
tk.Label(root, text="Longueur du mot de passe :", bg=BG_COLOR, fg=FG_COLOR, font=("Arial", 12)).pack(pady=8)
tk.Entry(root, textvariable=length_var, width=10, font=("Arial", 12), bg=ENTRY_BG, fg=FG_COLOR, insertbackground=FG_COLOR).pack()

tk.Checkbutton(root, text="Inclure des chiffres", variable=digits_var, bg=BG_COLOR, fg=FG_COLOR, selectcolor=BG_COLOR, font=("Arial", 11)).pack(pady=4)
tk.Checkbutton(root, text="Inclure des caractères spéciaux", variable=special_var, bg=BG_COLOR, fg=FG_COLOR, selectcolor=BG_COLOR, font=("Arial", 11)).pack(pady=4)

tk.Button(
    root,
    text="Générer",
    command=generate_password,
    font=("Arial", 12),
    bg=BTN_COLOR,
    fg=FR_COLOR_BTN,
    activebackground=BTN_COLOR,
    activeforeground=FR_COLOR_BTN
).pack(pady=12)

tk.Entry(root, textvariable=password_var, font=("Courier", 14), width=30, justify='center', state='readonly', bg=ENTRY_BG, fg="#00ffcc", readonlybackground=ENTRY_BG).pack(pady=10)

tk.Button(
    root,
    text="Copier",
    command=copy_to_clipboard,
    font=("Arial", 12),
    bg=BTN_COLOR,
    fg=FR_COLOR_BTN,
    activebackground=BTN_COLOR,
    activeforeground=FR_COLOR_BTN
).pack(pady=5)

# Barre + Label de force
tk.Label(root, text="Force du mot de passe :", bg=BG_COLOR, fg=FG_COLOR, font=("Arial", 11)).pack(pady=(10, 2))

bar_frame = tk.Frame(root, bg=BG_COLOR)
bar_frame.pack(pady=2)

strength_bar = tk.Frame(bar_frame, bg="grey", height=10, width=200)
strength_bar.pack(side="left")

strength_label = tk.Label(bar_frame, text="⏳", bg=BG_COLOR, fg=FG_COLOR, font=("Arial", 11), padx=10)
strength_label.pack(side="left")

# Lancement
root.mainloop()