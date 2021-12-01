from pdf2image import convert_from_path
from pytesseract import *
import pyautogui
from PIL import Image
from pytesseract import *
#putanja do tesseract foldera, jako bitno!!!!
pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract"


#putanja se unosi ispod:
path_to_pdf = "C:\ds\ocr-fica.pdf"


def convert_pdf_to_img(pdf_file):
    """
    @desc: this function converts a PDF into Image
        @params:
        - pdf_file: the file to be converted
        @returns:
        - an interable containing image format of all the pages of the PDF
    """
    return convert_from_path(pdf_file)


def convert_image_to_text(file):
    """
    @desc: this function extracts text from image
        @params:
        - file: the image file to extract the content
        @returns:
        - the textual content of single image
    """
    
    text = image_to_string(file)
    return text


def get_text_from_any_pdf(pdf_file):
    """
    @desc: this function is our final system combining the previous functions
        @params:
        - file: the original PDF File
        @returns:
        - the textual content of ALL the pages
    """
    images = convert_pdf_to_img(pdf_file)
    final_text = ""
    for pg, img in enumerate(images):
        
        final_text += convert_image_to_text(img)
        #print("Page n°{}".format(pg))
        #print(convert_image_to_text(img))
    
    return final_text

print(get_text_from_any_pdf(path_to_pdf))
