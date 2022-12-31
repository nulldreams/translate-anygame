import cv2
import ctypes
import pytesseract
import pyscreenshot
from deep_translator import GoogleTranslator
from pynput.keyboard import Key, Listener

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def translate():
    pic = pyscreenshot.grab(bbox=(2080, 850, 3100, 1350))
    pic.save("image.png")

    import numpy as np 
    import cv2 
    from matplotlib import pyplot as plt 
    # Reading image from folder where it is stored 
    img = cv2.imread('image.png') 
    # denoising of image saving it into dst image 
    dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 15) 
    # Plotting of source and destination image 
    plt.subplot(121), plt.imshow(img) 
    plt.subplot(122), plt.imshow(dst) 
    plt.show()

    text = pytesseract.image_to_string(dst)

    translated = GoogleTranslator(source='english', target='portuguese').translate(text)

    ctypes.windll.user32.MessageBoxW(0, translated, "Your title", 1)
