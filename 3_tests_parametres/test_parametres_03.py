"""
Tester plusieurs scénarios: un test par scénario
"""
from romains import romains


def test_romains_0():
    assert romains(0) == ""


def test_romains_1():
    assert romains(1) == "I"


def test_romains_2():
    assert romains(2) == "II"


def test_romains_3():
    assert romains(3) == "III"


def test_romains_4():
    assert romains(4) == "IV"


def test_romains_5():
    assert romains(5) == "V"


def test_romains_9():
    assert romains(9) == "IX"


def test_romains_10():
    assert romains(10) == "X"


def test_romains_20():
    assert romains(20) == "XX"


def test_romains_50():
    assert romains(50) == "L"


def test_romains_100():
    assert romains(100) == "C"


def test_romains_400():
    assert romains(400) == "CD"


def test_romains_500():
    assert romains(500) == "D"


def test_romains_1000():
    assert romains(1000) == "M"


def test_romains_1976():
    assert romains(1976) == "MCMLXXVI"
