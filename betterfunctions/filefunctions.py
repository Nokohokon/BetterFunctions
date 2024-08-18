import os

# Dateiverwaltungsfunktionen


def file_size(file_path: str, size_type: str = "KB"):
    """Returns the size of a file.

    Parameters
    ----------
    file_path:
        The path of the file.
    size_type:
        The size type in which the result should be displayed. Defaults to KB.

    Return
    ------
    :class:`str`
        The size as a string.
    """
    if size_type == "KB":
        r = f"{os.path.getsize(file_path) / 1024} Kilobyte"

    elif size_type == "MB":
        r = f"{os.path.getsize(file_path) / 1024 / 1024} Megabyte"

    elif size_type == "GB":
        r = f"{os.path.getsize(file_path) / 1024 / 1024 / 1024} Gigabyte"
    else:
        raise("Please insert a regular size type like KB (kilobyte), MB (megabyte) or GB (gigabyte).")
    return r


def list_files_in_directory(directory: str):
    """Lists all files in a given directory.

    Parameters
    ----------
    directory:
        The directory from which the items should be displayed.

    Return
    ------
    :class:`list`
        The list of all files.
    """
    return os.listdir(directory)


def create_directory(directory: str):
    """Creates a new directory.

    Parameters
    ----------
    directory:
        The name of the new directory.

    """
    os.makedirs(directory, exist_ok=True)


def delete_file(file_path: str):
    """Deletes a file.

    Parameters
    ----------
    file_path:
        The path of the file.
    """
    os.remove(file_path)


def create_text_file(text: str, directory: str | None = None, filename: str = "file.txt"):
    """
    Creates a text file in a directory with given name and given text.

    Parameters
    ----------
    directory:
        The directory where the file should be created. Default's to None.
    text:
        The text, which should be in the created file.
    filename:
        The name of the created file.
    """

    if not text:
        raise("Please insert a text into the function.")
    # Take the current directory if none is given.
    if directory is None:
        directory = os.getcwd()

    # Create the path to the file.
    file_path = os.path.join(directory, filename)

    try:
        # Open the file in writing-mode and paste the text in.
        with open(file_path, 'w') as file:
            file.write(text)
        print(f"File '{filename}' succesfully created at '{directory}'.")
    except Exception as e:
        print(f"Error by creating the file: {e}")
