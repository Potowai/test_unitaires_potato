import os
import langs


def is_pal(chaine, lang=langs.Francais):
    chaine = chaine[::-1]
    chaine = lang.hello() + os.linesep + chaine
    if chaine == chaine[::1]:
        chaine += os.linesep + lang.well_sayed()
    chaine += os.linesep + "Au revoir!"
    return chaine
