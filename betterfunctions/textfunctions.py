import string
import os
import fnmatch
from pathlib import Path

# Textverarbeitungsfunktionen


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


    Returns
    -------
    :class:`int`

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
    """Counts the words in a given string.

    Parameters
    ---------
    text:
        The string used to count the words.

    Returns
    -------
    :class:`int`
    """
    words = text.split()
    return len(words)


def reverse_string(s: str):
    """Reverses a given string.

    Parameters
    ----------
    s:
        The string which should be reversed.

    Returns
    -------
    :class:`str`
    """
    return s[::-1]


def remove_punctuation(text: str):
    """Removes punctuation from a given string.

    Parameters
    ----------

    text:
        The string, whom you want to remove the punctuation from.

    Returns
    -------
    :class:`str`
    """
    return ''.join(char for char in text if char not in string.punctuation)


def replace_substring(text: str, old: str, new: str):
    """Replaces a substring with a new text.

    Parameters
    ----------
    text:
        The string where the substring is in.
    old:
        The old substring.
    new:
        The new content of the substring.

    Returns
    -------
    :class:`str`

    """
    return text.replace(old, new)


def to_snake_case(text: str):
    """Converts a string to snake case.

    Parameters
    ----------
    text:
        The string which should be converted.

    Returns
    -------
    :class:`str`
    """
    return text.lower().replace(" ", "_")


def to_camel_case(text: str):
    """Converts a string to camelcase.

    Parameters
    ----------
    text:
        The string which should be converted.


    Returns
    -------
    :class:`str`
    """
    words = text.split()
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])
