import fitz
import io
from pdfminer.high_level import extract_text
from PIL import Image
import pytesseract
import docx2txt as d2t
import os

pytesseract.pytesseract.tesseract_cmd = r'D:\ReaderStuff\tesseract.exe'

#PDF
def PdfText(pdf_path):
    text = extract_text(pdf_path)

    #images in pdf
    pdf = fitz.open(pdf_path)
    for i in range(len(pdf)):
        page = pdf[i]
        images = page.get_images()
        for image in images:
            base_img = pdf.extract_image(image[0])
            image_data = base_img["image"]
            img = Image.open(io.BytesIO(image_data))
            ocr_text = pytesseract.image_to_string(img)
            text += "\n[Image OCR Text]:\n" + ocr_text
    return text

#IMG
def ImgText(img_path):
    img = Image.open(img_path)
    return pytesseract.image_to_string(img)

#WORD
def DocxText (path_to_file, image_folder="temp_docx_images", get_text=True):
    os.makedirs(image_folder, exist_ok=True)
    text = d2t.process(path_to_file, image_folder)

    #images in docx
    for filename in os.listdir(image_folder):
        if filename.lower().endswith((".jpg", "jpeg", ".png")):
            img_path = os.path.join(image_folder, filename)
            ocr_text = ImgText(img_path)
            text += f"\n[OCR from image {filename}]:\n{ocr_text}"

    return text if get_text else ""

#TXT
def TxtText (path):
    with open(path, encoding="utf-8") as f:
        return f.read()