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

def extract_skills(text):
    doc = nlp(text.lower())

    found_skills = []

    for skill in skills_list:
        if skill in text.lower():
            found_skills.append(skill)

    return list(set(found_skills))
