"""
Assertions relatives aux appels à des fonctions (1)
"""


def repete(f, n, *args, **kwargs):
    for _ in range(n):
        f(*args, **kwargs)


def test_repete():
    appels = []

    def mock_f(*args, **kwargs):
        nonlocal appels
        appels.append((args, kwargs))

    repete(mock_f, 2, "toto", titi=42)

    assert len(appels) == 2
    for param in appels:
        assert param == (("toto",), {'titi': 42})
