import string
import os
import fnmatch
from pathlib import Path

## Textverarbeitungsfunktionen
def count_lines(
    directory: str | None = None,
    *,
    count_empty_lines: bool = True,
    include_hidden: bool = False,
    ignored_dirs: list[str] | None = None,
    ignored_files: list[str] | None = None,
) -> int:
    """Counts the total amount of lines in all Python files in the given directory.

    Parameters
    ----------
    directory:
        The directory to count the lines in. Defaults to the current working directory.
    count_empty_lines:
        Whether to count empty lines. Defaults to ``True``.
    include_hidden:
        Whether to include directories starting with a dot. Defaults to ``False``.
    ignored_dirs:
        A list of directories to ignore. By default, venv folders and folders starting with a dot
        are ignored.
    ignored_files:
        A list of file patterns to ignore.
    """
    if directory is None:
        directory = os.getcwd()
    if ignored_dirs is None:
        ignored_dirs = []
    if ignored_files is None:
        ignored_files = []

    total_lines = 0
    for root, _, files in os.walk(directory):
        if not include_hidden and Path(root).parts[-1].startswith("."):
            ignored_dirs.append(root)
        if "pyvenv.cfg" in files:  # ignore venv folders
            ignored_dirs.append(root)

        if any([True for pattern in ignored_dirs if pattern in str(Path(root))]):
            continue

        for file in files:
            if not file.endswith(".py"):
                continue

            if any([True for pat in ignored_files if fnmatch.fnmatch(file, pat)]):
                continue

            file_path = os.path.join(root, file)
            with open(file_path, errors="ignore") as f:
                for line in f:
                    if not count_empty_lines and line.strip() == "":
                        continue
                    total_lines += 1

    return total_lines

def word_count(text: str):
    """Zählt die Anzahl der Wörter in einem gegebenen Text.

    Parameters
    ---------
    text:
        Der Text, aus welchem die Wörter gezählt werden sollen.
    """
    words = text.split()
    return len(words)


def reverse_string(s: str):
    """Kehrt einen gegebenen String um.

    Parameters
    ----------
    s:
        Der String welcher umgekehrt werden soll.
    """
    return s[::-1]


def remove_punctuation(text: str):
    """Entfernt Satzzeichen aus einem gegebenen Text.

    Parameters
    ----------

    text:
        Der Text, aus welchem Satzzeichen entfernt werden soll
    """
    return ''.join(char for char in text if char not in string.punctuation)


def replace_substring(text: str, old: str, new: str):
    """Ersetzt ein Substring durch einen neuen String.

    Parameters
    ----------
    text:
        Der Text, in welchem die Änderung erfolgen soll
    old:
        Der zu ersetzende Text.
    new:
        Der ersetzte Text.

    """
    return text.replace(old, new)


def to_snake_case(text:str):
    """Wandelt einen String in snake_case um.

    Parameters
    ----------
    text:
        Der Text welcher umgewandelt werden soll.

    """
    return text.lower().replace(" ", "_")


def to_camel_case(text:str):
    """Wandelt einen String in camelCase um.

    Parameters
    ----------
    text:
        Der Text welcher umgewandelt werden soll.

    """
    words = text.split()
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])
