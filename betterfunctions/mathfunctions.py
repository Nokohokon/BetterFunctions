import math

# Mathematische Funktionen


def format_number(number: int, *, decimal_places: int = 1, trailing_zero: bool = False) -> str:
    """Formats a big number into a tiny, readable format.

    Parameters
    ----------
    number:
        The number which should be formatted.
    decimal_places:
        The amount of decimal places which should be displayed. Defaults to 1.
    trailing_zero:
        Should trailing zeros be displayed? Default: False.

    Returns
    -------
    :class:`str`
        The formatted number.
    """

    suffix = ""
    if number >= 1_000_000_000 or number <= -1_000_000_000:
        txt = f"{number / 1_000_000_000:.{decimal_places}f}"
        suffix = "B"
    elif number >= 1_000_000 or number <= -1_000_000:
        txt = f"{number / 1_000_000:.{decimal_places}f}"
        suffix = "M"
    elif number >= 100 or number <= -100:
        txt = f"{number / 1_000:.{decimal_places}f}"
        suffix = "K"
    else:
        txt = str(number)

    if not trailing_zero:
        txt = txt.rstrip("0").rstrip(".")

    return txt + suffix


def fibonacci(n: int):
    """Generates a list with the fibonacci-numbers to n.

    Parameters
    ----------
    n:
        The number to where the fibonaccis should be generated.

    Returns
    -------
    :class:`list`
        The list with the fibonaccis.
    """
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


def is_prime(num: int):
    """Checks if a number is a prime number.

    Parameters
    ----------
    num:
        The number which should be checked.

    Returns
    -------
    :class:`boolean`
        The result as a boolean.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_numbers(n: int):
    """Generates a list with the prime numbers to n.

    Parameters
    ----------
    n:
        The number, to where the prime numbers should be generated.

    Returns
    -------
    :class:`list`
        The list with the prime numbers.
    """
    return [x for x in range(2, n + 1) if is_prime(x)]


def gcd(a: int, b: int):
    """Calculates the gcd of two numbers.

    Parameters
    ----------
    a:
        The first number.
    b:
        The second number.

    Returns
    -------
    :class:`int`
        The gcd of both numbers.
    """
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int):
    """Calculates the lcm of two numbers.

    Parameters
    ----------
    a:
        The first number.
    b:
        The second number.

    Returns
    -------
    :class:`int`
        The gcd of the both numbers.
    """
    return abs(a*b) // gcd(a, b)


def factorial(n: int):
    """Calculates the factorial of a number.

    Parameters
    ----------
    n:
        The number where the factorial should be calculated.

    Returns
    -------
    :class:`int`
        The factorial of the given umber.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def celsius_to_fahrenheit(celsius: float):
    """Converts celsius to fahrenheit.

    Parameters
    ----------
    celsius:
        The temperature in fahrenheit.

    Returns
    -------
    :class:`int`
        The converted temperature.
    """
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit: float):
    """Converts fahrenheit to celsius.

    Parameters
    ----------
    fahrenheit:
        The temperature in fahrenheit.

    Returns
    -------
    :class:`int`
        The converted temperature.
    """
    return (fahrenheit - 32) * 5/9


def int_to_roman(num: int):
    """Converts an integer to a roman number.

    Parameters
    ----------
    num:
        The number which should be converted.

    Returns
    -------
    :class:`str`
        The converted roman number.
    """
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num


def distance_between_points(x1: float, y1: float, x2: float, y2: float):
    """Calculates the distance between two points.

    Parameters
    ----------
    x1:
        The x-Coordinate of the first point.
    x2:
        The x-Coordinate of the second point.
    y1:
        The y-Coordinate of the first point.
    y2:
        The y-Coordinate of the second point.

    Returns
    -------
    :class:`int`
        The calculated distance as a integer.
    """
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
