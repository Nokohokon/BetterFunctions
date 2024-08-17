import string

## Textverarbeitungsfunktionen

def word_count(text):
    """Zählt die Anzahl der Wörter in einem gegebenen Text."""
    words = text.split()
    return len(words)


def reverse_string(s):
    """Kehrt einen gegebenen String um."""
    return s[::-1]


def remove_punctuation(text):
    """Entfernt Satzzeichen aus einem gegebenen Text."""
    return ''.join(char for char in text if char not in string.punctuation)


def replace_substring(text, old, new):
    """Ersetzt ein Substring durch einen neuen String."""
    return text.replace(old, new)


def to_snake_case(text):
    """Wandelt einen String in snake_case um."""
    return text.lower().replace(" ", "_")


def to_camel_case(text):
    """Wandelt einen String in camelCase um."""
    words = text.split()
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])
