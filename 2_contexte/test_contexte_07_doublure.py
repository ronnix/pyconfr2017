"""
Utilisation de doublures : injection
"""
import pytest


class APIMeteo:
    def temperature(self, ville):
        raise NotImplementedError  # requete HTTP...


class Temps:
    def __init__(self, api_meteo):
        self.api_meteo = api_meteo

    def il_va_faire_chaud(self, ville):
        return self.api_meteo.temperature(ville) > 20


@pytest.fixture
def api_meteo():

    class FausseAPIMeteo:
        valeurs = {
            'Lille': 17,
            'Toulouse': 24,
        }

        def temperature(self, ville):
            return self.valeurs[ville]

    return FausseAPIMeteo()


@pytest.fixture
def temps(api_meteo):
    return Temps(api_meteo)


def test_il_va_faire_chaud(temps):
    assert temps.il_va_faire_chaud('Toulouse') is True


def test_il_ne_va_pas_faire_chaud(temps):
    assert temps.il_va_faire_chaud('Lille') is False
