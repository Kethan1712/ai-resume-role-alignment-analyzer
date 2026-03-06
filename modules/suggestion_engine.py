# modules/suggestion_engine.py

def generate_suggestions(semantic_score, missing_skills, top_sentences):
    """
    Generates role-aware, identity-preserving suggestions.
    """

    suggestions = []

    # Semantic alignment logic
    if semantic_score < 0.4:
        suggestions.append("Strong role mismatch detected.")
        suggestions.append("Consider restructuring summary to better reflect job expectations.")
        suggestions.append("Highlight role-specific technical contributions and measurable impact.")
    elif semantic_score < 0.7:
        suggestions.append("Moderate alignment detected.")
        suggestions.append("Improve project descriptions to better match required responsibilities.")
        suggestions.append("Add measurable outcomes where possible.")
    else:
        suggestions.append("Good overall alignment with the job role.")
        suggestions.append("Minor refinements may improve impact.")

    # Skill gap logic
    if missing_skills:
        suggestions.append("Consider highlighting experience related to the following skills:")
        for skill in missing_skills:
            suggestions.append(f"- {skill}")
    else:
        suggestions.append("All required technical skills are present.")

    # Strong sections
    suggestions.append("Most relevant resume sections (consider expanding these):")
    for sentence, score in top_sentences[:2]:
        suggestions.append(f"- {sentence}")

    return suggestions