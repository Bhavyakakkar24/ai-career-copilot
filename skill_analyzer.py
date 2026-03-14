import spacy

nlp = spacy.load("en_core_web_sm")

skills_list = [
    "python",
    "java",
    "c++",
    "machine learning",
    "data analysis",
    "sql",
    "power bi",
    "excel",
    "deep learning",
    "nlp",
    "flask",
    "django",
    "tensorflow",
    "pandas"
]

role_skills = {
    "Data Analyst": [
        "python",
        "sql",
        "power bi",
        "excel",
        "statistics",
        "data visualization"
    ],
    "Machine Learning Engineer": [
        "python",
        "machine learning",
        "deep learning",
        "tensorflow",
        "pandas",
        "numpy"
    ],
    "Backend Developer": [
        "python",
        "django",
        "flask",
        "sql",
        "api",
        "docker"
    ]
}

def extract_skills(text):
    text = text.lower()
    doc = nlp(text)

    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))


def skill_gap_analysis(user_skills, role):
    required = role_skills.get(role, [])

    user_skills = [skill.lower() for skill in user_skills]

    missing = [skill for skill in required if skill.lower() not in user_skills]

    return missing
