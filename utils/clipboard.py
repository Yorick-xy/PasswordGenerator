### utils/clipboard.py
import pyperclip
from tkinter import messagebox

def copy_to_clipboard(password):
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copié", "Mot de passe copié dans le presse-papiers !")
    else:
        messagebox.showwarning("Vide", "Aucun mot de passe à copier.")