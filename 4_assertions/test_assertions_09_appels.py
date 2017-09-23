"""
Assertions relatives aux appels à des fonctions (3)
"""
from unittest.mock import Mock


def repete(f, n, *args, **kwargs):
    for _ in range(n):
        f(*args, **kwargs)


def test_repete():
    mock_f = Mock()

    repete(mock_f, 1, "toto", titi=42)

    mock_f.assert_called_once_with("toto", titi=42)
