import os

## Dateiverwaltungsfunktionen



def file_size(file_path):
    """Gibt die Größe einer Datei in Kilobyte zurück."""
    return os.path.getsize(file_path) / 1024, "Kilobyte"


def list_files_in_directory(directory):
    """Listet alle Dateien in einem Verzeichnis auf."""
    return os.listdir(directory)


def create_directory(directory):
    """Erstellt ein neues Verzeichnis."""
    os.makedirs(directory, exist_ok=True)


def delete_file(file_path):
    """Löscht eine Datei."""
    os.remove(file_path)
