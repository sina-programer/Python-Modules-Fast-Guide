import mimetypes

filename = 'file.csv'
mime = mimetypes.guess_type(filename)
print(mime)

if mime[0]:
    file_type = mime[0].split('/', 1)[0]
    print(file_type)
