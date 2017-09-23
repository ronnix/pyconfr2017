"""
Test basé sur des propriétés (*property-based testing*)

3. Utilisation d'hypothesis pour trouver automatiquement
   des exemples qui font échouer notre test

Cf. http://hypothesis.readthedocs.io/

"""
from hypothesis import given
from hypothesis.strategies import text, integers

from chiffrement import chiffrer, dechiffrer


@given(text(min_size=1), integers())
def test_chiffrement(texte, decalage):
    assert chiffrer(texte, decalage) != texte


@given(text(), integers())
def test_reversibilite(texte, decalage):
    texte_chiffre = chiffrer(texte, decalage)
    assert dechiffrer(texte_chiffre, decalage) == texte
