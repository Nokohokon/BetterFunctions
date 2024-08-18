import sys


# Benutzereingabefunktionen


def intput(prompt: str = "Please insert an integer: "):
    """Asks for an integer and returns the input as an int.

    Parameters
    ----------
    prompt:
        The wanted prompt for the input.

    Returns
    -------
    :class:`int`
    """
    while True:
        try:
            return int(input(prompt))  # Converts the input to an integer
        except ValueError:
            print("Wrong input. Please insert a number.")


def floatput(prompt: str = "Please insert a float: "):
    """Asks for a float and returns the input as a float.

    Parameters
    ----------
    prompt:
        Die gewünschte Aufforderung.

    Returns
    -------
    :class:`float`
    """
    while True:
        try:
            return float(input(prompt))  # Converts the input into a float.
        except ValueError:
            print("Wrong input. Please insert a float.")


def yes_no_input(prompt: str = "Please answer with yes or no: "):
    """Asks for a yes or no. Returns the input as a boolean.

    Parameters
    ---------
    prompt:
        The wanted prompt.

    Returns
    -------
    :class:`bool`
    """
    while True:
        answer = input(prompt).lower()
        if answer in ["j", "ja", "y", "yes"]:
            return True
        elif answer in ["n", "nein", "no"]:
            return False
        else:
            print("Wrong input. Please answer with yes or no.")


def wait_for_key(prompt: str = "Press a key to continue..."):
    """Waits for the user to press a key.

    Parameters
    ----------
    prompt:
        The prompt which should be displayed in the console.
    """
    print(prompt, end="")
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
