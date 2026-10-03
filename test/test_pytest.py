import os
import sys

import pytest

# Make the project root importable so `from src import calculator` works
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import calculator


def test_fun1():
    assert calculator.fun1(2, 3) == 5
    assert calculator.fun1(5, 0) == 5
    assert calculator.fun1(-1, 1) == 0
    assert calculator.fun1(-1, -1) == -2


def test_fun2():
    assert calculator.fun2(2, 3) == -1
    assert calculator.fun2(5, 0) == 5
    assert calculator.fun2(-1, 1) == -2
    assert calculator.fun2(-1, -1) == 0


def test_fun3():
    assert calculator.fun3(2, 3) == 6
    assert calculator.fun3(5, 0) == 0
    assert calculator.fun3(-1, 1) == -1
    assert calculator.fun3(-1, -1) == 1


def test_fun4():
    assert calculator.fun4(2, 3, 5) == 10
    assert calculator.fun4(5, 0, -1) == 4
    assert calculator.fun4(-1, -1, -1) == -3
    assert calculator.fun4(-1, -1, 100) == 98


# Parametrized example (see Step 4 of the lab README): the same test function
# runs once per (x, y, expected) tuple.
@pytest.mark.parametrize(
    "x, y, expected",
    [
        (2, 3, 5),
        (5, 0, 5),
        (-1, 1, 0),
        (-1, -1, -2),
    ],
)
def test_fun1_parametrized(x, y, expected):
    assert calculator.fun1(x, y) == expected


def test_fun1_raises_on_non_numbers():
    with pytest.raises(ValueError):
        calculator.fun1("2", 3)
