import pytest

from calculator import operations


def test_addition():
    assert operations.add(2, 3) == 5
    assert operations.add(-1, 1) == 0
    assert operations.add(0, 0) == 0


def test_subtraction():
    assert operations.subtract(5, 3) == 2
    assert operations.subtract(-1, -1) == 0
    assert operations.subtract(0, 5) == -5


def test_multiplication():
    assert operations.multiply(2, 3) == 6
    assert operations.multiply(-1, 1) == -1
    assert operations.multiply(0, 5) == 0


def test_division():
    assert operations.divide(6, 3) == 2
    assert operations.divide(-4, 2) == -2
    assert operations.divide(5, 2) == 2.5

    with pytest.raises(ValueError):
        operations.divide(5, 0)

def test_average():
    values = [7, 5, 6]
    assert operations.average(values) == 4

    values = [7, 5, 6, 1]
    assert operations.average(values) == 4