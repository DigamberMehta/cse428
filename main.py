from extraction import extract_text_from_file

def main(file_path):
    # Step 1: Extract text from the file
    text = extract_text_from_file(file_path)
    if not text:
        print("Text extraction failed.")
        return
    
    print("Text extraction successful!" , text)

# Example usage
if __name__ == "__main__":
    file_path = "/Users/digamber/Desktop/ML/cse428/resume_sample/resume.docx"  # Replace with your file path
    main(file_path)
