from extraction import extract_text_from_file
from processing import preprocess_text

def main(file_path):
    # Step 1: Extract text from the file
    text = extract_text_from_file(file_path)
    if not text:
        print("Text extraction failed.")
        return
    
    print("Text extraction successful!" , text)
    
    # Step 2: Process the text with spaCy
    structured_data = preprocess_text(text)
    
    # Step 3: Display the structured information
    print("\nExtracted Structured Information:")
    print(f"Entities: {structured_data['entities']}")
    print(f"Skills: {structured_data['skills']}")
    print(f"Education: {structured_data['education']}")

# Example usage
if __name__ == "__main__":
    file_path = "C:\\Users\\digam\\Desktop\\Gen AI\\machine\\ML\\resume_sample\\resume.docx"  # Replace with your file path
    main(file_path)
