from stub_lang import StubLang
from src.finder import is_pal

__lang = StubLang
__chaine = "default"


def build(chaine=__chaine, lang=__lang):
    return is_pal(chaine, lang)
