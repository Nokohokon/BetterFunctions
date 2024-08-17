import sys
## Benutzereingabefunktionen



def intput(prompt="Bitte gib eine Ganzzahl ein: "):
    """Fragt den Benutzer nach einer Ganzzahl und gibt diese als Integer zurück.

    Parameters
    ----------
    prompt:
        Die gewünschte Aufforderung.

    """
    while True:
        try:
            return int(input(prompt))  # Konvertiert die Eingabe in eine Ganzzahl
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine gültige Zahl ein.")


def floatput(prompt="Bitte gib eine Gleitzahl ein: "):
    """Fragt den Benutzer nach einer Zahl und gibt diese als Float zurück.

    Parameters
    ----------
    prompt:
        Die gewünschte Aufforderung.

    """
    while True:
        try:
            return float(input(prompt))  # Konvertiert die Eingabe in eine Gleitkommazahl
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine gültige Zahl ein.")


def yes_no_input(prompt="Bitte antworte mit Ja oder Nein: "):
    """Fragt den Benutzer nach einer Ja/Nein-Antwort und gibt True oder False zurück.

    Parameters
    ---------
    prompt:
        Die gewünschte Aufforderung.
    """
    while True:
        answer = input(prompt).lower()
        if answer in ["j", "ja", "y", "yes"]:
            return True
        elif answer in ["n", "nein", "no"]:
            return False
        else:
            print("Ungültige Eingabe. Bitte antworte mit Ja oder Nein.")


def wait_for_key():
    """Wartet darauf, dass der Benutzer eine Taste drückt."""
    print("Drücke eine beliebige Taste, um fortzufahren...", end="")
    if sys.platform.startswith('win'):
        import msvcrt
        msvcrt.getch()
    else:
        import termios
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)
        new[3] = new[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, new)
        try:
            sys.stdin.read(1)
        except IOError:
            pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, old)
    print("\r                     \r", end="")
