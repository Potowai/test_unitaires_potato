import os
import langs


def is_pal(chaine, lang=langs.Francais):
    chaine = chaine[::-1]
    text = lang.hello() + os.linesep + chaine
    if chaine == chaine[::-1]:
        text += os.linesep + lang.well_sayed()
    text += os.linesep + lang.bye()
    return text
