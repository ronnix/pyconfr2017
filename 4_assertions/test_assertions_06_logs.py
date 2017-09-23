"""
Assertions relatives aux logs
"""
import logging


def affiche_moyenne(nombres):
    if nombres:
        print(sum(nombres) / len(nombres))
    else:
        logging.error("liste vide")


def test_sortie_standard(capsys):
    affiche_moyenne([1, 2, 3, 4])
    out, err = capsys.readouterr()
    assert out == "2.5\n"


def test_sortie_erreur(caplog):
    affiche_moyenne([])
    assert "liste vide" in caplog.text
