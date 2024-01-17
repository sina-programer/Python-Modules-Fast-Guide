import glob

EXTENSION = '.py'
files = glob.glob('*'+EXTENSION)
print('\n'.join(files))
