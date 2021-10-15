# used this to start me off  https://www.youtube.com/watch?v=dRyFS2p9SqM&ab_channel=FalconInfomatic
import pytesseract  #install this on cpu before pip install,  also make sure folder for it is in (86)program file
from PIL import Image 
import pathlib
from pathlib import Path
from pdf2image import convert_from_path # for changing pdf to jpg, 
import fitz  #trying this instead of poppler
import os
import fnmatch

working_directory = Path(__file__).absolute().parent
scanned_pdf = working_directory / 'hp.pdf'

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe" #exe file for using ocr 

doc = fitz.open(scanned_pdf)
for i in range(len(doc)):
    page = doc.loadPage(i)  # number of page
    pix = page.getPixmap()
    output = f"outfile{i}.png"
    pix.writePNG(output)

    text=pytesseract.image_to_string(output) 
    print(text)


 