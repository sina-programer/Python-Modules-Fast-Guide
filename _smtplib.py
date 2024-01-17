import smtplib

USERNAME = 'username@gmail.com'
PASSWORD = ''
SERVER = 'smtp.gmail.com'
PORT = 465  # 587 for TLS

TO = 'another.username@gmail.com'
SUBJECT = 'Subject'
TEXT = 'your text'
MESSAGE = """To: {to}
Subject: {subject}
{body}"""

server = smtplib.SMTP_SSL(SERVER, PORT)
server.login(USERNAME, PASSWORD)
server.sendmail(USERNAME, TO, MESSAGE.format(to=TO, subject=SUBJECT, body=TEXT))
server.close()
