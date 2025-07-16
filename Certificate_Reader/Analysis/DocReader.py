import fitz
import io
from pdfminer.high_level import extract_pages, extract_text
from PIL import Image
import pytesseract
import doc2txt as d2t


#PDF
def PdfText(pdf_path):
    return extract_text(pdf_path)

#IMG
def ImgText(img_path):
    pytesseract.pytesseract.tesseract_cmd = r'D:\ReaderStuff\tesseract.exe'
    img = Image.open(img_path)
    return pytesseract.image_to_string(img)

#WORD
def DocxText (path_to_file, image_folder=None, get_text=True):
    text = d2t.process(path_to_file, image_folder)
    return text if get_text else ""

#TXT
def TxtText (path):
    with open(path, encoding="utf-8") as f:
        return f.read