import spacy
import re

nlp = spacy.load("en_core_web_sm")

# Predefined skills for matching
PREDEFINED_SKILLS = ["Python", "JavaScript", "React", "CSS", "Node.js", "Express.js", "Bootstrap", "SQL", "Django", "AWS"]

def extract_email(text):
    """Extract email addresses using regex."""
    match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return match.group(0) if match else None

def extract_links(text):
    """Extract LinkedIn or other URLs using regex."""
    urls = re.findall(r'(https?://[^\s]+)', text)
    return urls

def group_education(entities):
    """Combine degree, field, and institution into structured education entries."""
    education = []
    current_entry = {}
    for text, label in entities:
        if label == "ORG" and "University" in text:
            current_entry["institution"] = text
        elif "Bachelor" in text or "Master" in text or "PhD" in text:
            current_entry["degree"] = text
        elif "CSE" in text or "Computer Science" in text:
            current_entry["field"] = text
        
        if len(current_entry) == 3:  # Once all details are captured
            education.append(current_entry)
            current_entry = {}
    return education

def preprocess_text(text):
    """Process extracted text with spaCy for structured information."""
    doc = nlp(text)
    
    # Extract named entities
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    # Extract predefined skills
    skills = [skill for skill in PREDEFINED_SKILLS if skill in text]
    
    # Extract email and links
    email = extract_email(text)
    links = extract_links(text)
    
    # Extract education details
    education = group_education(entities)
    
    # Structure the extracted data
    structured_data = {
        "entities": entities,
        "skills": skills,
        "education": education,
        "email": email,
        "links": links,
    }
    return structured_data
