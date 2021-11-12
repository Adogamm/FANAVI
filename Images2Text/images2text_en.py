import os
import cv2
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'

class Image2Text:
    
    def image_to_text():
        path = r'C:\\Fanavi\\images\\screenshot.png'
        image = cv2.imread(path)
        text = pytesseract.image_to_string(image)
        return text