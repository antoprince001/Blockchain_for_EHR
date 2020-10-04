#try:
from PIL import Image
#except ImportError:
 #   import Image
import pytesseract

def ocr_core(images):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(images))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

print(ocr_core('sample1.jpg'))