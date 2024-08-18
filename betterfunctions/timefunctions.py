import datetime
import pytz


# Zeit Funktionen


def current_date(timezone='UTC'):
    """Returns the current date in the specified timezone.

    Parameters
    ----------
    timezone : :class:`str`, optional
        The timezone for which to return the date, specified as a UTC offset in the format 'UTC[+-]HH:MM', defaults to 'UTC'.

    Return
    ------
    :class:`str`
        The current date in the format "dd.mm.yyyy".
    """
    if timezone.startswith('UTC'):
        tz = pytz.FixedOffset(pytz.utc_offset_timedelta(timezone))
    else:
        tz = pytz.timezone(timezone)
    return datetime.datetime.now(tz).strftime("%d.%m.%Y")


def current_time(timezone='UTC'):
    """Returns the current time in the specified timezone.

    Parameters
    ----------
    timezone : :class:`str`, optional
        The timezone for which to return the time, specified as a UTC offset in the format 'UTC[+-]HH:MM', defaults to 'UTC'.

    Return
    ------
    :class:`str`
        The current time in the format "HH:MM:SS".
    """
    if timezone.startswith('UTC'):
        tz = pytz.FixedOffset(pytz.utc_offset_timedelta(timezone))
    else:
        tz = pytz.timezone(timezone)
    return datetime.datetime.now(tz).strftime("%H:%M:%S")

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
