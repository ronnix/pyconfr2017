"""
Assertions relatives aux appels à des fonctions (2)
"""
from unittest.mock import Mock, call


def repete(f, n, *args, **kwargs):
    for _ in range(n):
        f(*args, **kwargs)


def test_repete():
    mock_f = Mock()

    repete(mock_f, 2, "toto", titi=42)

    assert mock_f.called

    assert mock_f.call_count == 2

    mock_f.assert_has_calls([
        call("toto", titi=42),
        call("toto", titi=42),
    ])
