import os


def is_pal(chaine):
    chaine = chaine[::-1]
    chaine = "Bonjour" + os.linesep + chaine
    if chaine == chaine[::1]:
        chaine += os.linesep + "Bien dit!"
    chaine += os.linesep + "Au revoir!"
    return chaine
