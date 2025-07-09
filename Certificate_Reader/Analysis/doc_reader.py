import re
import fitz
import PIL.Image
import io
import tabula
from pdfminer.high_level import extract_pages, extract_text

for page_layout in extract_pages("example.pdf"):
    for element in page_layout:
        print(element)

pdf = fitz.open("example.pdf")
counter = 1
for i in range(len(pdf)):
    page = pdf[i]
    images = page.get_images()
    for image in images:
        base_img = pdf.extract_image(image[0])
        image_data = base_img["image"]
        img = PIL.Image.open(io.BytesIO(image_data))
        extension = base_img["ext"]
        img.save(open(f"image{counter}.{extension}", "wb"))
        counter += 1

tables = tabula.read_pdf("example.pdf", pages="all")
df = tables[0]


