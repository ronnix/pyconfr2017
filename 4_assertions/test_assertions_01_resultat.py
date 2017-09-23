"""
Assertions relatives au résultat
"""


def moyenne(nombres):
    return sum(nombres) / len(nombres)


def test_valeur():
    assert moyenne([1, 2, 3, 4]) == 2.5
