"""
Cycle de vie d'une fixture py.test
"""
from tempfile import NamedTemporaryFile
import os

import pytest


def ajoute_ligne(nom_de_fichier, message):
    with open(nom_de_fichier, "a") as f:
        f.write(message + "\n")


@pytest.yield_fixture(scope='function')  # valeur par défaut
# @pytest.yield_fixture(scope='session')
def nom_de_fichier():
    with NamedTemporaryFile(mode='w', delete=False) as temp:
        yield temp.name
    os.remove(temp.name)


def test_ajoute_une_ligne(nom_de_fichier):
    ajoute_ligne(nom_de_fichier, 'bonjour')

    with open(nom_de_fichier) as f:
        assert f.readlines() == [
            'bonjour\n',
        ]


def test_ajoute_plusieurs_lignes(nom_de_fichier):
    ajoute_ligne(nom_de_fichier, 'bonjour')
    ajoute_ligne(nom_de_fichier, 'le monde')

    with open(nom_de_fichier) as f:
        assert f.readlines() == [
            'bonjour\n',
            'le monde\n',
        ]
