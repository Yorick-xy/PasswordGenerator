### main.py
from tkinter import Tk
from ui.layout import build_interface
from config.theme import BG_COLOR

def main():
    root = Tk()
    root.title("🔐 Générateur de mot de passe")
    root.geometry("420x420")
    root.configure(bg=BG_COLOR)
    root.resizable(False, False)

    build_interface(root)

    root.mainloop()

if __name__ == "__main__":
    main()