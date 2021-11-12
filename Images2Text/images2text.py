import os
import cv2
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'

class Image2Text:
    def image_to_text(image):
        text = pytesseract.image_to_string(image,lang="spa")
        return text

path = r'C:\\Fanavi\\images\\screenshot.png'
imagenprueba = cv2.imread(path)
prueba = Image2Text
print(prueba.image_to_text(imagenprueba))