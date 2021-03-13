# test_tesseract.py

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Peter\Anaconda3\envs\tesseract\Library\bin\tesseract.exe'

text_from_image = pytesseract.image_to_string(Image.open('images/test_image.png'))
print(text_from_image)
