"""
Transcription d'un nombre en chiffres romains
"""


def romains(nombre):
    return (
        ("I" * nombre)
        .replace("IIIIIIIIII", "X")
        .replace("IIIIIIIII", "IX")
        .replace("IIIII", "V")
        .replace("IIII", "IV")
        .replace("XXXXXXXXXX", "C")
        .replace("XXXXXXXXX", "XC")
        .replace("XXXXX", "L")
        .replace("CCCCCCCCCC", "M")
        .replace("CCCCCCCCC", "CM")
        .replace("CCCCC", "D")
        .replace("CCCC", "CD")
    )
