"""
Tester plusieurs scénarios: un seul test, et plusieurs assertions (1)
"""
from romains import romains


def test_romains():
    assert romains(0) == ""
    assert romains(1) == "I"
    assert romains(2) == "II"
    assert romains(3) == "III"
    assert romains(4) == "IV"
    assert romains(5) == "V"
    assert romains(9) == "IX"
    assert romains(10) == "X"
    assert romains(20) == "XX"
    assert romains(50) == "L"
    assert romains(100) == "C"
    assert romains(400) == "CD"
    assert romains(500) == "D"
    assert romains(1000) == "M"
    assert romains(1976) == "MCMLXXVI"
