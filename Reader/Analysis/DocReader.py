import fitz
import io
from pdfminer.high_level import extract_text
from PIL import Image, ImageFilter
import pytesseract
import docx2txt as d2t
import os
import shutil
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'D:\ReaderStuff\tesseract.exe'

#IMG
def ImagText(img_path, SelectedLang):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
    _, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    coords = np.column_stack(np.where(img > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = img.shape[:2]
    M = cv2.getRotationMatrix2D((w // 2, h // 2), angle, 1.0)
    img = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    img = cv2.equalizeHist(img)
    pil_img = Image.fromarray(img)
    return pytesseract.image_to_string(pil_img, SelectedLang)

#PDF
def PdfText(pdf_path, SelectedLang):
    text = extract_text(pdf_path)

    #images in pdf
    pdf = fitz.open(pdf_path)
    for i in range(len(pdf)):
        page = pdf[i]
        images = page.get_images()
        for image in images:
            base_img = pdf.extract_image(image[0])
            image_data = base_img["image"]
            temp_img_path = f"temp_pdf_img_{i}_{image[0]}.png"
            with open(temp_img_path, "wb") as img_file:
                img_file.write(image_data)
            ocr_text = ImagText(temp_img_path, SelectedLang)
            text += f"\n[Image OCR Text]:\n{ocr_text}"
            os.remove(temp_img_path)
    return text

#WORD
def DocxText (path_to_file, image_folder="temp_docx_images", get_text=True):
    os.makedirs(image_folder, exist_ok=True)
    text = d2t.process(path_to_file, image_folder)

    #images in docx
    for filename in os.listdir(image_folder):
        if filename.lower().endswith((".jpg", "jpeg", ".png")):
            img_path = os.path.join(image_folder, filename)
            ocr_text = ImagText(img_path)
            text += f"\n[OCR from image {filename}]:\n{ocr_text}"
    shutil.rmtree(image_folder)
    return text if get_text else ""


#TXT
def TxtText (path):
    with open(path, encoding="utf-8") as f:
        return f.read()