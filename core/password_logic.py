### core/password_logic.py
import random
import string

def generate_password(length, use_digits=True, use_special=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("Aucun jeu de caractères sélectionné.")

    return ''.join(random.choice(characters) for _ in range(length))