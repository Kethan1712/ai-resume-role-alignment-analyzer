# modules/skill_extractor.py

# Predefined skill list (can expand later or load from external file)
SKILL_SET = [
    "python", "java", "c", "c++", "machine learning",
    "deep learning", "nlp", "tensorflow", "pytorch",
    "sql", "mongodb", "html", "css", "javascript",
    "react", "node", "data analysis", "aws",
    "docker", "kubernetes"
]

def extract_skills(text):
    """
    Extracts known technical skills from text.
    """
    text_lower = text.lower()
    found_skills = []

    for skill in SKILL_SET:
        if skill in text_lower:
            found_skills.append(skill)

    return list(set(found_skills))


def match_skills(resume_skills, jd_skills):
    """
    Compares resume skills with job description skills.
    """
    resume_set = set(resume_skills)
    jd_set = set(jd_skills)

    matching = resume_set.intersection(jd_set)
    missing = jd_set - resume_set

    if len(jd_set) > 0:
        alignment_score = (len(matching) / len(jd_set)) * 100
    else:
        alignment_score = 0

    return list(matching), list(missing), alignment_score