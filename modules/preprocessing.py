# modules/preprocessing.py

import spacy

# Load spaCy model once
nlp = spacy.load("en_core_web_sm")

def preprocess(text):
    """
    Cleans and normalizes text using NLP preprocessing.
    """
    doc = nlp(text)
    tokens = [
        token.lemma_.lower()
        for token in doc
        if not token.is_stop and not token.is_punct
    ]
    return " ".join(tokens)

def get_sentences(text):
    """
    Splits text into sentences.
    """
    doc = nlp(text)
    return [sent.text.strip() for sent in doc.sents]