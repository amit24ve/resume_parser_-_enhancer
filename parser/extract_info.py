import spacy
import fitz
import re

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    return "\n".join([page.get_text() for page in doc])

def extract_resume_info(text):
    doc = nlp(text)
    lines = text.split("\n")
    name = doc.ents[0].text if doc.ents else "Unknown"

    email = re.search(r"[a-zA-Z0-9\._%+-]+@[a-zA-Z0-9\.-]+\.[a-zA-Z]{2,}", text)
    phone = re.search(r"(\+?\d{1,3})?[\s\-]?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{4}", text)

    skills = []
    for line in lines:
        if "skills" in line.lower():
            idx = lines.index(line)
            skills = lines[idx + 1].strip().split(",")
            break

    education = [line for line in lines if re.search(r"(B\.Tech|Bachelor|Master|Diploma)", line)]
    experience = [line for line in lines if re.search(r"(Intern|Engineer|Developer|Experience|Company)", line)]

    return {
        "Name": name,
        "Email": email.group() if email else "Not found",
        "Phone": phone.group() if phone else "Not found",
        "Skills": [s.strip() for s in skills],
        "Education": education,
        "Experience": experience
    }
