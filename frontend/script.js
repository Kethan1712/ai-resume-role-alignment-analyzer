const radius = 60;
const circumference = 2 * Math.PI * radius;

function setProgress(circle, percent) {
    const offset = circumference - (percent / 100) * circumference;
    circle.style.strokeDashoffset = offset;
}

function getColor(percent) {
    if (percent >= 70) return "#22c55e";     // green
    if (percent >= 40) return "#f59e0b";     // amber
    return "#ef4444";                        // red
}

function getLabel(percent) {
    if (percent >= 70) return "Strong Alignment";
    if (percent >= 40) return "Moderate Alignment";
    return "Needs Improvement";
}

async function analyzeResume() {

    const button = document.getElementById("analyzeBtn");
    button.innerText = "Analyzing...";
    button.disabled = true;

    const resumeText = document.getElementById("resumeText").value;
    const jobText = document.getElementById("jobText").value;

    if (!resumeText || !jobText) {
        alert("Please enter both Resume and Job Description.");
        button.innerText = "Analyze Resume";
        button.disabled = false;
        return;
    }

    const response = await fetch("https://resume-analyzer-api-nj1m.onrender.com/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            resume_text: resumeText,
            job_description: jobText
        })
    });

    const data = await response.json();

    const skillScore = data.skill_alignment_score;
    const semanticScore = data.semantic_similarity_score;

    document.getElementById("skillScore").innerText = skillScore + "%";
    document.getElementById("semanticScore").innerText = semanticScore + "%";

    const skillRing = document.getElementById("skillRing");
    const semanticRing = document.getElementById("semanticRing");

    skillRing.style.stroke = getColor(skillScore);
    semanticRing.style.stroke = getColor(semanticScore);

    setProgress(skillRing, skillScore);
    setProgress(semanticRing, semanticScore);

    document.getElementById("skillLabel").innerText = getLabel(skillScore);
    document.getElementById("semanticLabel").innerText = getLabel(semanticScore);

    // Matching Skills
    const matchingDiv = document.getElementById("matchingSkills");
    matchingDiv.innerHTML = "";
    data.matching_skills.forEach(skill => {
        const span = document.createElement("span");
        span.className = "skill-badge";
        span.innerText = skill;
        matchingDiv.appendChild(span);
    });

    // Missing Skills
    const missingDiv = document.getElementById("missingSkills");
    missingDiv.innerHTML = "";
    data.missing_skills.forEach(skill => {
        const span = document.createElement("span");
        span.className = "skill-badge missing";
        span.innerText = skill;
        missingDiv.appendChild(span);
    });

    // Top Sentences
    const sentenceList = document.getElementById("topSentences");
    sentenceList.innerHTML = "";
    data.top_relevant_sentences.forEach(item => {
        const li = document.createElement("li");
        li.innerText = `${item.score}% — ${item.sentence}`;
        sentenceList.appendChild(li);
    });

    // Suggestions
    const suggestionList = document.getElementById("suggestions");
    suggestionList.innerHTML = "";
    data.suggestions.forEach(suggestion => {
        const li = document.createElement("li");
        li.innerText = suggestion;
        suggestionList.appendChild(li);
    });

    document.getElementById("results").classList.remove("hidden");

    button.innerText = "Analyze Resume";
    button.disabled = false;
}