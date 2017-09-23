"""
Mise en place d'un contexte avec setUp
"""
from unittest import TestCase


def compte(valeur, sequence):
    n = 0
    for element in sequence:
        if element == valeur:
            n += 1
    return n


class TestCompte(TestCase):

    def setUp(self):
        self.exemple = [2, 1, 2, 2, 3]

    def test_compte_absent(self):
        assert compte(4, self.exemple) == 0

    def test_compte_multiple(self):
        assert compte(2, self.exemple) == 3
