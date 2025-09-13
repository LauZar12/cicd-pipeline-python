from typing import Union

# Just the type alias for numbers.
Number = Union[int, float]


# Basic calculator functions.
def add(a: Number, b: Number) -> Number:
    return a + b


def subtract(a: Number, b: Number) -> Number:
    return a - b


def multiply(a: Number, b: Number) -> Number:
    return a * b


def divide(a: Number, b: Number) -> Number:
    if b == 0:
        raise ValueError("You cannot divide by zero.")
    return a / b
