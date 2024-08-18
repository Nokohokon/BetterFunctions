import string
import random


# Zufallsfunktionen


def generate_password(length: int = 12, include_special: bool = True):
    """Generates a random password with the given length.

    Parameters
    ----------

    length:
        The length of the passwor. Defaults to 12.
    include_special:
        Should special characters be included? Defaults to True

    Returns
    -------
    :class:`str`
    """
    characters = string.ascii_letters + string.digits
    if include_special:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def random_color():
    """Generates a random hex-color.

    Returns
    -------
    :class:`str`
    """
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))


def random_choice(items: list):
    """Chooses a random element from a list.

    Parameters
    ----------
    items:
        The list including the elements.

    Returns
    -------
        random choice, class depends on the list.

    """
    return random.choice(items)


def shuffle_list(items: list):
    """Shuffles a list randomly.

    Parameters
    ----------
    items:
        The list with the items.

    Returns
    -------
    :class:`list`
    """
    random.shuffle(items)
    return items
