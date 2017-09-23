"""
Nettoyage d'un contexte avec tearDown
"""
from tempfile import NamedTemporaryFile
from unittest import TestCase
import os


def mots(nom_de_fichier):
    with open(nom_de_fichier) as fichier:
        contenu = fichier.read()
    return contenu.split(' ')


class TestMots(TestCase):

    def setUp(self):
        with NamedTemporaryFile(mode='w', delete=False) as temp:
            temp.write("bonjour le monde")
            temp.flush()
        self.nom_de_fichier = temp.name

    def tearDown(self):
        os.remove(self.nom_de_fichier)

    def test_mots(self):
        assert mots(self.nom_de_fichier) == [
            'bonjour',
            'le',
            'monde',
        ]
