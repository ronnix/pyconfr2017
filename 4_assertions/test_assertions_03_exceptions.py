"""
Assertions relatives aux exceptions (2)
"""
import pytest


def moyenne(nombres):
    return sum(nombres) / len(nombres)


def test_valeur():
    assert moyenne([1, 2, 3, 4]) == 2.5


def test_erreur():
    with pytest.raises(ZeroDivisionError) as exc_info:
        moyenne([])
    assert str(exc_info.value) == "division by zero"
