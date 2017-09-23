"""
Tester plusieurs scénarios: un seul test, et plusieurs assertions (2)
"""
from romains import romains


EXEMPLES = [
    (0, ""),
    (1, "I"),
    (2, "II"),
    (3, "III"),
    (4, "IV"),
    (5, "V"),
    (9, "IX"),
    (10, "X"),
    (20, "XX"),
    (50, "L"),
    (100, "C"),
    (400, "CD"),
    (500, "D"),
    (1000, "M"),
    (1976, "MCMLXXVI"),
]


def test_romains():
    for nombre, attendu in EXEMPLES:
        assert romains(nombre) == attendu
