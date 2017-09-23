"""
Assertions relatives à la sortie standard
"""
import sys


def affiche_moyenne(nombres):
    if nombres:
        print(sum(nombres) / len(nombres))
    else:
        print("liste vide", file=sys.stderr)


def test_sortie_standard(capsys):
    affiche_moyenne([1, 2, 3, 4])
    out, err = capsys.readouterr()
    assert out == "2.5\n"


def test_sortie_erreur(capsys):
    affiche_moyenne([])
    out, err = capsys.readouterr()
    assert err == "liste vide\n"
