import pytest


def add_one(x):
    return x + 1


def test_add_one():
    number = 3
    result = add_one(number)

    assert result == 4
