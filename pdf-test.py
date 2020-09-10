import os
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


def convert_single(fn):
    """Converts pdf, returns its text content as a string"""
    manager = PDFResourceManager()
    output = StringIO()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)
    with open(fn, 'rb') as infile:
        for page in PDFPage.get_pages(infile, set(),caching=True, check_extractable=True):
            interpreter.process_page(page)
            convertedPDF = output.getvalue()

    converter.close()
    output.close()
    return convertedPDF

def convert_all(pdfDir, txtDir):
    """Convert all the PDFs in a folder"""
    for pdf in os.listdir(pdfDir): #iterate through pdfs in input directory 
        fileExtension = os.path.splitext(pdf)[1]
        if fileExtension == ".pdf":
            pdfFilename = pdfDir + pdf
            text = convert_single(pdfFilename) #get string of text content of pdf
            textFilename = txtDir + pdf[:-4] + ".txt"
            with open(textFilename, 'w') as textFile:
                textFile.write(text)


pdfDir = "pdf_input_dir/"
txtDir = "out_txt/"
convert_all(pdfDir, txtDir)
print('look it finished')