# main.py

from modules.parser import load_text
from modules.preprocessing import preprocess, get_sentences
from modules.skill_extractor import extract_skills, match_skills
from modules.semantic_engine import document_similarity, sentence_level_alignment
from modules.suggestion_engine import generate_suggestions


# Load files
resume_text = load_text("data/resume.txt")
jd_text = load_text("data/job_description.txt")

print("Resume Loaded Successfully")
print("Job Description Loaded Successfully")


# Preprocessing
clean_resume = preprocess(resume_text)
clean_jd = preprocess(jd_text)

print("\nClean Resume Sample:\n")
print(clean_resume[:300])

print("\nClean Job Description Sample:\n")
print(clean_jd[:300])


# Skill Extraction
resume_skills = extract_skills(resume_text)
jd_skills = extract_skills(jd_text)

matching_skills, missing_skills, alignment_score = match_skills(resume_skills, jd_skills)

print("\nResume Skills Found:", resume_skills)
print("Job Description Skills Found:", jd_skills)
print("Matching Skills:", matching_skills)
print("Missing Skills:", missing_skills)
print(f"Skill Alignment Score: {alignment_score:.2f}%")


# Semantic Analysis
semantic_score = document_similarity(resume_text, jd_text)
print(f"\nSemantic Similarity Score: {semantic_score * 100:.2f}%")


# Sentence-Level Alignment
resume_sentences = get_sentences(resume_text)
sentence_scores = sentence_level_alignment(resume_sentences, jd_text)

print("\nTop Relevant Resume Sentences:")
for sentence, score in sentence_scores[:3]:
    print(f"{score*100:.2f}% - {sentence}")


# Suggestions
suggestions = generate_suggestions(semantic_score, missing_skills, sentence_scores)

print("\nRole-Aware Suggestions:")
for suggestion in suggestions:
    print("-", suggestion)