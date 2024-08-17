import string
import random


## Zufallsfunktionen


def generate_password(length=12, include_special=True):
    """Generiert ein zufälliges Passwort mit der angegebenen Länge."""
    characters = string.ascii_letters + string.digits
    if include_special:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def random_color():
    """Generiert eine zufällige Farbe im Hex-Format."""
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))


def random_choice(items):
    """Wählt zufällig ein Element aus einer Liste aus."""
    return random.choice(items)


def shuffle_list(items):
    """Mischt eine Liste zufällig."""
    random.shuffle(items)
    return items
