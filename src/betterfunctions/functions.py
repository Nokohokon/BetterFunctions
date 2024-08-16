import random
import string
import os
import sys

class functions:
    @staticmethod
    def fibonacci(n):
        """Generiert eine Liste der Fibonacci-Zahlen bis n."""
        fib_sequence = [0, 1]
        while fib_sequence[-1] + fib_sequence[-2] <= n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

    @staticmethod
    def is_prime(num):
        """Überprüft, ob eine Zahl prim ist."""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    @staticmethod
    def prime_numbers(n):
        """Generiert eine Liste der Primzahlen bis n."""
        return [x for x in range(2, n + 1) if BetterFunctions.is_prime(x)]

    @staticmethod
    def generate_password(length=12):
        """Generiert ein zufälliges Passwort mit der angegebenen Länge."""
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    @staticmethod
    def word_count(text):
        """Zählt die Anzahl der Wörter in einem gegebenen Text."""
        words = text.split()
        return len(words)

    @staticmethod
    def reverse_string(s):
        """Kehrt einen gegebenen String um."""
        return s[::-1]

    @staticmethod
    def random_color():
        """Generiert eine zufällige Farbe im Hex-Format."""
        return "#{:06x}".format(random.randint(0, 0xFFFFFF))

    @staticmethod
    def file_size(file_path):
        """Gibt die Größe einer Datei in Kilobyte zurück."""
        return os.path.getsize(file_path) / 1024

    @staticmethod
    def random_choice(items):
        """Wählt zufällig ein Element aus einer Liste aus."""
        return random.choice(items)

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Konvertiert Celsius in Fahrenheit."""
        return (celsius * 9/5) + 32

    @staticmethod
    def int_to_roman(num):
        """Konvertiert eine ganze Zahl in römische Ziffern."""
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syms[i]
                num -= val[i]
            i += 1
        return roman_num

    @staticmethod
    def output(obj):
        """Gibt das übergebene Objekt aus."""
        print(obj)

    @staticmethod
    def intput(prompt="Bitte gib eine Ganzzahl ein: "):
        """Fragt den Benutzer nach einer Ganzzahl und gibt diese als Integer zurück."""
        while True:
            try:
                return int(input(prompt))  # Konvertiert die Eingabe in eine Ganzzahl
            except ValueError:
                print("Ungültige Eingabe. Bitte gib eine gültige Zahl ein.")

    @staticmethod
    def floatput(prompt="Bitte gib eine Gleitzahl ein: "):
        """Fragt den Benutzer nach einer Zahl und gibt diese als Float zurück."""
        while True:
            try:
                return float(input(prompt)) # Konvertiert die Eingabe in eine Gleitkommazahl

            except ValueError:
                print("Ungültige Eingabe. Bitte gib eine gültige Zahl ein.")


    @staticmethod
    def yes_no_input(prompt="Bitte antworte mit Ja oder Nein: "):
        """Fragt den Benutzer nach einer Ja/Nein-Antwort und gibt True oder False zurück."""
        while True:
            answer = input(prompt).lower()
            if answer in ["j", "ja", "y", "yes"]:
                return True
            elif answer in ["n", "nein", "no"]:
                return False
            else:
                print("Ungültige Eingabe. Bitte antworte mit Ja oder Nein.")

    @staticmethod
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