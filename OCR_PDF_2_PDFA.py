#ocr Fica test
import os
import requests
import ocrmypdf
import pdfplumber

#putanja do pdf fajla
invoice="C:\\ds\\ocr-fica.pdf"

'''outp_inv="C:\\ds\\output.pdf"
with pdfplumber.open(outp_inv) as pdf:
    page=pdf.pages[0]
    text=page.extract_text()
    print(text)
    '''

os.system(f'ocrmypdf {invoice} output.pdf')



