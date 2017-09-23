"""
Nettoyage d'un contexte avec @pytest.yield_fixture
"""
from tempfile import NamedTemporaryFile
import os

import pytest


def mots(nom_de_fichier):
    with open(nom_de_fichier) as fichier:
        contenu = fichier.read()
    return contenu.split(' ')


@pytest.yield_fixture
def nom_de_fichier():
    with NamedTemporaryFile(mode='w', delete=False) as temp:
        temp.write("bonjour le monde")
        temp.flush()
        yield temp.name
    os.remove(temp.name)


def test_mots(nom_de_fichier):
    assert mots(nom_de_fichier) == [
        'bonjour',
        'le',
        'monde',
    ]
