"""
Chiffrement par décalage
"""


def chiffrer(texte, decalage=1):
    return ''.join(
        chr(ord(caractere) + decalage) for caractere in texte
    )


def dechiffrer(texte, decalage=1):
    return ''.join(
        chr(ord(caractere) - decalage) for caractere in texte
    )
