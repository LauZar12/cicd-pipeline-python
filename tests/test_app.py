"""Unit tests for the calculator module."""

import pytest

from app.calculator import add, divide, multiply, subtract


def test_add():
    """Test addition of two numbers."""
    assert add(2, 3) == 5


def test_subtract():
    """Test subtraction of two numbers."""
    assert subtract(5, 2) == 3


def test_multiply():
    """Test multiplication of two numbers."""
    assert multiply(3, 4) == 12


def test_divide():
    """Test division of two numbers."""
    assert divide(10, 2) == 5


def test_divide_by_zero():
    """Test that division by zero raises an error."""
    with pytest.raises(ValueError):
        divide(1, 0)
