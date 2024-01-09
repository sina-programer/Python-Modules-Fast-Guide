from captcha.image import ImageCaptcha

CLAUSE = 'SinaF123'

image = ImageCaptcha()
image.write(CLAUSE, f'captcha-{CLAUSE}.png')
