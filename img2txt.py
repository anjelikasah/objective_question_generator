import pytesseract
from PIL import Image
from main_algorithm import objective_generator

def image_to_text(imgs):
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
    text= pytesseract.image_to_string(imgs)
    text=text.replace ('\n', ' ')
    objective_generator(text)

