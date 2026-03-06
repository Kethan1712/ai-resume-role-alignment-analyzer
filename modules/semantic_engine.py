# modules/semantic_engine.py

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model once (very important)
model = SentenceTransformer('all-MiniLM-L6-v2')


def document_similarity(resume_text, jd_text):
    """
    Computes overall semantic similarity between resume and job description.
    """
    resume_embedding = model.encode(resume_text)
    jd_embedding = model.encode(jd_text)

    score = cosine_similarity(
        [resume_embedding],
        [jd_embedding]
    )[0][0]

    return score


def sentence_level_alignment(resume_sentences, jd_text):
    """
    Computes similarity of each resume sentence against job description.
    Returns sorted sentence scores.
    """
    jd_embedding = model.encode(jd_text)

    sentence_scores = []

    for sentence in resume_sentences:
        sentence_embedding = model.encode(sentence)
        score = cosine_similarity(
            [sentence_embedding],
            [jd_embedding]
        )[0][0]

        sentence_scores.append((sentence, score))

    # Sort highest first
    sentence_scores.sort(key=lambda x: x[1], reverse=True)

    return sentence_scores