import spacy
from spacy import displacy

sp = spacy.load('en_core_web_sm')


def space(text):
    sen = sp(text)
    for word in sen:
        vb = f'{word.text:{12}} {word.pos_:{10}} {word.tag_:{8}} {spacy.explain(word.tag_)}'
    return vb
