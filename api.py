from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from modules.preprocessing import preprocess, get_sentences
from modules.skill_extractor import extract_skills, match_skills
from modules.semantic_engine import document_similarity, sentence_level_alignment
from modules.suggestion_engine import generate_suggestions

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ResumeRequest(BaseModel):
    resume_text: str
    job_description: str


@app.post("/analyze")
def analyze_resume(data: ResumeRequest):

    resume_text = data.resume_text
    jd_text = data.job_description

    # Skills
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    matching_skills, missing_skills, alignment_score = match_skills(
        resume_skills, jd_skills
    )

    # Semantic similarity
    semantic_score = float(document_similarity(resume_text, jd_text))

    # Sentence alignment
    resume_sentences = get_sentences(resume_text)
    sentence_scores = sentence_level_alignment(resume_sentences, jd_text)

    # Suggestions
    suggestions = generate_suggestions(
        semantic_score, missing_skills, sentence_scores
    )

    return {
        "skill_alignment_score": round(alignment_score, 2),
        "semantic_similarity_score": round(semantic_score * 100, 2),
        "matching_skills": matching_skills,
        "missing_skills": missing_skills,
        "top_relevant_sentences": [
            {"sentence": s, "score": round(float(sc) * 100, 2)}
            for s, sc in sentence_scores[:3]
        ],
        "suggestions": suggestions
    }
@app.get("/")
def home():
    return {"message": "AI Resume Role Alignment Analyzer API is running"}