# This code is for reviewing word.docx files for specific kewords. 
# Terminal will ask for keywords you are looking for and will result in the file names that include the keyword(s) you are looking for. 

import os
import docx
import re

def read_word_document(file_path):
    doc = docx.Document(file_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + " "
    return text.lower()

def main():
    folder_path = r"path\to\folder\you\want\to\search"
    keywords = input("Enter keywords (comma-separated): ").lower().split(",")

    for filename in os.listdir(folder_path):
        if filename.endswith(".docx"):
            file_path = os.path.join(folder_path, filename)
            resume_text = read_word_document(file_path)
            for kw in keywords:
                if re.search(r'\b{}\b'.format(kw), resume_text):
                    print(f"Resume '{filename}' contains keyword: {kw}")

if __name__ == "__main__":
    main()
