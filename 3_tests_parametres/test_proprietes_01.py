"""
Test basé sur des propriétés (*property-based testing*)

1. Utilisation d'une liste d'exemples écrits par nous

"""
import pytest

from chiffrement import chiffrer, dechiffrer


EXEMPLES = [
    "bonjour les amis",
    "voilà l'été",
    "😀",
]


@pytest.mark.parametrize('texte', EXEMPLES)
def test_chiffrement(texte):
    assert chiffrer(texte) != texte


@pytest.mark.parametrize('texte', EXEMPLES)
def test_reversibilite(texte):
    texte_chiffre = chiffrer(texte)
    assert dechiffrer(texte_chiffre) == texte
