import qrcode  # pip install qrcode "qrcode[pil]"


DATA = 'Your desired data'
EXPORT_PATH = 'output.png'


# Simple
image_simple = qrcode.make(DATA)  # type(image) = qrcode.image.pil.PilImage
image_simple.save(EXPORT_PATH)


# Advanced (of course it's better)
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,  # the size of each box
    border=4,  # 4 is the minimum value
)
qr.add_data(DATA)
qr.make(fit=True)
image_advanced = qr.make_image(fill_color="black", back_color="white").convert('RGB')
image_advanced.save(EXPORT_PATH)


# %% Read the QRcode -------------------------------------

import cv2  # pip install opencv-python

image = cv2.imread(EXPORT_PATH)
detector = cv2.QRCodeDetector()
decoded_text, points, _ = detector.detectAndDecode(image)
print("Decoded text: ", decoded_text)
