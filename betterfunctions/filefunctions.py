import os

## Dateiverwaltungsfunktionen



def file_size(file_path: str ,type: str = "KB"):
    """Gibt die Größe einer Datei zurück.

    Parameters
    ----------
    file_path:
        Der Pfad der gewünschten Datei
    type:
        Der Größentyp, in welcher die Größe angegeben werden soll. Default: KB

    """
    if type == "KB":
        r = f"{os.path.getsize(file_path) / 1024} Kilobyte"

    elif type == "MB":
        r = f"{os.path.getsize(file_path) / 1024 / 1024} Megabyte"

    elif type == "GB":
        r = f"{os.path.getsize(file_path) / 1024 / 1024 / 1024} Gigabyte"
    else:
        raise("Please insert a regular size type like KB (kilobyte), MB (megabyte) or GB (gigabyte)")
    return r


def list_files_in_directory(directory: str):
    """Listet alle Dateien in einem Verzeichnis auf.

        Parameters
        ----------
        directory:
            Das Verzeichnis, aus  welchem die Dateien aufgelistet werden sollen.
    """
    return os.listdir(directory)


def create_directory(directory: str):
    """Erstellt ein neues Verzeichnis.

    Parameters
    ----------
    directory:
        Der Name des neuen Verzeichnisses

    """
    os.makedirs(directory, exist_ok=True)


def delete_file(file_path: str):
    """Löscht eine Datei.

        Parameters
        ----------
        file_path:
            Der Pfad zur Datei
    """
    os.remove(file_path)


def create_text_file(text: str,directory: str|None = None, filename: str ="file.txt"):
    if not text:
        raise("Please insert a text into the function.")
    """
    Erstellt eine Textdatei mit dem angegebenen Text und Dateinamen.

    :param directory: Das Verzeichnis, in dem die Datei erstellt werden soll.
                      Wenn None, wird das aktuelle Verzeichnis verwendet.
    :param text: Der Text, der in die Datei geschrieben werden soll.
    :param filename: Der Name der zu erstellenden Datei.
    """
    # Verwende das aktuelle Verzeichnis, wenn kein Verzeichnis angegeben ist
    if directory is None:
        directory = os.getcwd()

    # Erstelle den vollständigen Pfad zur Datei
    file_path = os.path.join(directory, filename)

    try:
        # Öffne die Datei im Schreibmodus und schreibe den Text hinein
        with open(file_path, 'w') as file:
            file.write(text)
        print(f"Datei '{filename}' erfolgreich erstellt in '{directory}'.")
    except Exception as e:
        print(f"Fehler beim Erstellen der Datei: {e}")