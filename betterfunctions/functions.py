import random
import string
import os
import sys
import math
import datetime

## Mathematische Funktionen

class MathFunctions:
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
        return [x for x in range(2, n + 1) if MathFunctions.is_prime(x)]

    @staticmethod
    def gcd(a, b):
        """Berechnet den größten gemeinsamen Teiler zweier Zahlen."""
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def lcm(a, b):
        """Berechnet das kleinste gemeinsame Vielfache zweier Zahlen."""
        return abs(a*b) // MathFunctions.gcd(a, b)

    @staticmethod
    def factorial(n):
        """Berechnet die Fakultät einer Zahl."""
        if n == 0:
            return 1
        else:
            return n * MathFunctions.factorial(n-1)

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Konvertiert Celsius in Fahrenheit."""
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        """Konvertiert Fahrenheit in Celsius."""
        return (fahrenheit - 32) * 5/9

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
    def distance_between_points(x1, y1, x2, y2):
        """Berechnet die Entfernung zwischen zwei Punkten."""
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

## Textverarbeitungsfunktionen

class TextFunctions:
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
    def remove_punctuation(text):
        """Entfernt Satzzeichen aus einem gegebenen Text."""
        return ''.join(char for char in text if char not in string.punctuation)

    @staticmethod
    def replace_substring(text, old, new):
        """Ersetzt ein Substring durch einen neuen String."""
        return text.replace(old, new)

    @staticmethod
    def to_snake_case(text):
        """Wandelt einen String in snake_case um."""
        return text.lower().replace(" ", "_")

    @staticmethod
    def to_camel_case(text):
        """Wandelt einen String in camelCase um."""
        words = text.split()
        return words[0].lower() + ''.join(word.capitalize() for word in words[1:])

## Zufallsfunktionen

class RandomFunctions:
    @staticmethod
    def generate_password(length=12, include_special=True):
        """Generiert ein zufälliges Passwort mit der angegebenen Länge."""
        characters = string.ascii_letters + string.digits
        if include_special:
            characters += string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    @staticmethod
    def random_color():
        """Generiert eine zufällige Farbe im Hex-Format."""
        return "#{:06x}".format(random.randint(0, 0xFFFFFF))

    @staticmethod
    def random_choice(items):
        """Wählt zufällig ein Element aus einer Liste aus."""
        return random.choice(items)

    @staticmethod
    def shuffle_list(items):
        """Mischt eine Liste zufällig."""
        random.shuffle(items)
        return items

## Dateiverwaltungsfunktionen

class FileFunctions:
    @staticmethod
    def file_size(file_path):
        """Gibt die Größe einer Datei in Kilobyte zurück."""
        return os.path.getsize(file_path) / 1024

    @staticmethod
    def list_files_in_directory(directory):
        """Listet alle Dateien in einem Verzeichnis auf."""
        return os.listdir(directory)

    @staticmethod
    def create_directory(directory):
        """Erstellt ein neues Verzeichnis."""
        os.makedirs(directory, exist_ok=True)

    @staticmethod
    def delete_file(file_path):
        """Löscht eine Datei."""
        os.remove(file_path)

## Benutzereingabefunktionen

class UserInputFunctions:
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
                return float(input(prompt))  # Konvertiert die Eingabe in eine Gleitkommazahl
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

## Zusätzliche Funktionen

class TimeFunctions:
    @staticmethod
    def current_date():
        """Gibt das aktuelle Datum zurück."""
        return datetime.date.today().strftime("%d.%m.%Y")

    @staticmethod
    def current_time():
        """Gibt die aktuelle Uhrzeit zurück."""
        return datetime.datetime.now().strftime("%H:%M:%S")

    @staticmethod
    def is_leap_year(year):
        """Überprüft, ob ein Jahr ein Schaltjahr ist."""
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
