import os
from PyPDF2 import PdfReader
import docx
from tika import parser

# Function to extract text from PDF files
def extract_text_from_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            reader = PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        print(f"Error extracting PDF text: {e}")
        return None

# Function to extract text from DOCX files
def extract_text_from_docx(file_path):
    try:
        doc = docx.Document(file_path)
        text = ""
        for para in doc.paragraphs:
            text += para.text + '\n'
        return text
    except Exception as e:
        print(f"Error extracting DOCX text: {e}")
        return None

# Function to extract text from text files
def extract_text_from_txt(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error extracting TXT text: {e}")
        return None

# Function to extract text using Tika (for handling multiple document formats)
def extract_text_using_tika(file_path):
    try:
        raw = parser.from_file(file_path)
        return raw.get('content', '')
    except Exception as e:
        print(f"Error extracting text using Tika: {e}")
        return None

# Main function to determine file type and call the appropriate extraction function
def extract_text_from_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower()

    if file_extension == '.pdf':
        print("PDF file detected.")
        return extract_text_from_pdf(file_path)
    
    elif file_extension == '.docx':
        print("DOCX file detected.")
        return extract_text_from_docx(file_path)
    
    elif file_extension == '.txt':
        print("Text file detected.")
        return extract_text_from_txt(file_path)
    
    else:
        print(f"Unsupported file type: {file_extension}")
        return extract_text_using_tika(file_path)
