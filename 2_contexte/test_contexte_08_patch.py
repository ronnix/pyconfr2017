"""
Utilisation de doublures : monkey patching
"""
from unittest.mock import patch

import pytest


class FausseAPIMeteo:
    valeurs = {
        'Lille': 17,
        'Toulouse': 24,
    }

    def temperature(self, ville):
        return self.valeurs[ville]


@pytest.fixture
def temps():
    from temps import Temps
    with patch('temps.APIMeteo', new=FausseAPIMeteo):
        return Temps()


def test_il_va_faire_chaud(temps):
    assert temps.il_va_faire_chaud('Toulouse') is True


def test_il_ne_va_pas_faire_chaud(temps):
    assert temps.il_va_faire_chaud('Lille') is False
