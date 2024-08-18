import datetime

# Zeit Funktionen


def current_date():
    """Returns the current date.

    Return
    ------
    :class:`str`
    """
    return datetime.date.today().strftime("%d.%m.%Y")


def current_time():
    """Returns the current time.

    Return
    ------
    :class:`str`
    """
    return datetime.datetime.now().strftime("%H:%M:%S")


def is_leap_year(year: int):
    """Checks if a year is a leap year.

    Parameters
    ----------
    year:
        The year which should be checked.

    Returns
    -------
    :class:`bool`
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
