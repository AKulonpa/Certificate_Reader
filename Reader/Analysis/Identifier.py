import os
from DocReader import (PdfText, TxtText, ImagText, DocxText)

def AnalyzeFile(filepath):
    ext = os.path.splitext(filepath)[1].lower()

    if ext == ".pdf":
        print("This is PDF...")
        text = PdfText(filepath)
        return text
    
    elif ext in [".jpg", ".jpeg", ".png"]:
        print("This is a picture...")
        text = ImagText(filepath)
        return text
    
    elif ext == ".docx":
        print("This is a word document...")
        text = DocxText(filepath)
        return text
    
    elif ext == ".txt":
        print("This is a text file...")
        text = TxtText(filepath)
        return text
    
    else:
        raise ValueError(f"I don't know what file this is :(")
    
