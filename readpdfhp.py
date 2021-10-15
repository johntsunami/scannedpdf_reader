# https://www.youtube.com/watch?v=dRyFS2p9SqM&ab_channel=FalconInfomatic

import pytesseract  #install this on cpu before pip install,  also make sure folder for it is in (86)program file
from PIL import Image 
import pathlib
from pathlib import Path

working_directory = Path(__file__).absolute().parent
pdfpic = working_directory / 'hppic.jpg'

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe" #exe file for using ocr 

#open PDF
#screen shot each page?
#Save each pic as names page1,page2, etc

img=Image.open(pdfpic) #to get image from our pc 
text=pytesseract.image_to_string(img) 
print(text)
 