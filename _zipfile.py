import zipfile


def create(path, files):
    if not path.endswith('.zip'):
        path += '.zip'
    with zipfile.ZipFile(path, 'w') as handler:
        for file in files:
            handler.write(file)

def extract(path):
    if zipfile.is_zipfile(path):
        with zipfile.ZipFile(path, 'r') as handler:
            handler.extractall()

def add(zip_path, file_path):
    if zipfile.is_zipfile(zip_path):
        with zipfile.ZipFile(zip_path, 'w') as handler:
            handler.write(file_path)

def file_list(path):
    if zipfile.is_zipfile(path):
        with zipfile.ZipFile(path) as handler:
            return handler.namelist()

def read(zip_path, file_path):
    if zipfile.is_zipfile(zip_path):
        with zipfile.ZipFile(zip_path) as zip_handler:
            with zip_handler.open(file_path) as file_handler:
                return file_handler.read()
