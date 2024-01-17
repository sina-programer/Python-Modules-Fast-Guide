from barcode.writer import ImageWriter  # pip install python-barcode
from barcode import EAN13

OUTPUT_PATH = 'barcode.png'
CONTENT = 100000100222345  # must be a number for EAN13
CONTENT = str(CONTENT)

writer = ImageWriter(format='PNG', mode='RGB')

with open(OUTPUT_PATH, 'wb') as handler:
    EAN13(CONTENT, writer=writer).write(handler)
