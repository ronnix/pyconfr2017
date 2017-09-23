"""
Test basé sur des propriétés (*property-based testing*)

2. Utilisation d'hypothesis pour trouver automatiquement
   des exemples qui font échouer notre test

Cf. http://hypothesis.readthedocs.io/

"""
from hypothesis import given
# from hypothesis import example
from hypothesis.strategies import text

from chiffrement import chiffrer, dechiffrer


# @given(text(min_size=1))
@given(text())
def test_chiffrement(texte):
    assert chiffrer(texte) != texte


@given(text())
# @example("bonjour les amis")
# @example("voilà l'été")
# @example("😀")
def test_reversibilite(texte):
    texte_chiffre = chiffrer(texte)
    assert dechiffrer(texte_chiffre) == texte
