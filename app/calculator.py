"""Calculator module with operation functions."""

from typing import Union

# Just the type alias for numbers.
Number = Union[int, float]


# Basic calculator functions.
def add(a: Number, b: Number) -> Number:
    """Return the sum of a and b."""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return the difference of a and b."""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Return the product of a and b."""
    return a * b


def divide(a: Number, b: Number) -> Number:
    """Return the quotient of a divided by b.
    Raises an error when b is zero. c:
    """
    if b == 0:
        raise ValueError("You cannot divide by zero.")
    return a / b
