"""
Mise en place d'un contexte avec @pytest.fixture
"""
import pytest


def compte(valeur, sequence):
    n = 0
    for element in sequence:
        if element == valeur:
            n += 1
    return n


@pytest.fixture
def exemple():
    return [2, 1, 2, 2, 3]


def test_compte_absent(exemple):
    assert compte(4, exemple) == 0


def test_compte_multiple(exemple):
    assert compte(2, exemple) == 3
