import random
import string
import os
import sys
import math
import datetime

## Mathematische Funktionen



def fibonacci(n):
    """Generiert eine Liste der Fibonacci-Zahlen bis n."""
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


def is_prime(num):
    """Überprüft, ob eine Zahl prim ist."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_numbers(n):
    """Generiert eine Liste der Primzahlen bis n."""
    return [x for x in range(2, n + 1) if is_prime(x)]


def gcd(a, b):
    """Berechnet den größten gemeinsamen Teiler zweier Zahlen."""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Berechnet das kleinste gemeinsame Vielfache zweier Zahlen."""
    return abs(a*b) // gcd(a, b)


def factorial(n):
    """Berechnet die Fakultät einer Zahl."""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def celsius_to_fahrenheit(celsius):
    """Konvertiert Celsius in Fahrenheit."""
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Konvertiert Fahrenheit in Celsius."""
    return (fahrenheit - 32) * 5/9


def int_to_roman(num):
    """Konvertiert eine ganze Zahl in römische Ziffern."""
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


def distance_between_points(x1, y1, x2, y2):
    """Berechnet die Entfernung zwischen zwei Punkten."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
