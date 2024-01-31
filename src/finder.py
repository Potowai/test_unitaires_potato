import os


def is_pal(chaine):
    if chaine == chaine[::1]:
        return chaine + os.linesep + "Bien dit!"
    return chaine[::-1]
