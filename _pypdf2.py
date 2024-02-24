#این کد یک سری اطلاعات در مورد PDF انتخابی ما به ما می دهد
from PyPDF2 import PdfFileReader as PDFReader
from pprint import pprint

def get_info(pdf):
    info = pdf.getDocumentInfo()
    return {
        'author': info.author,
        'creator': info.creator,
        'producer': info.producer,
        'subject': info.subject,
        'title': info.title,
        'pages': pdf.getNumPages(),
        'encrypted': pdf.getIsEncrypted()
    }


def get_text(pdf):
    # return list(map(lambda page: page.extractText(), pdf.pages))
    for idx in pdf.getNumPages():
        page = pdf.getPage(idx)
        yield page.extractText()


if __name__ == '__main__':
    path = input('Enter the PDF path: ')
    pdf = PDFReader(path)
    information = get_info(pdf)
    pprint(information)
