import csv


def write(filepath, content, header=None, encoding='utf-8', mode='w'):
    with open(filepath, mode, encoding=encoding, newline='') as handler:
        writer = csv.writer(handler)
        if header:
            writer.writerow(header)
        for row in content:
            writer.writerow(row)


def read(filepath, encoding='utf-8'):
    with open(filepath, encoding=encoding, newline='') as handler:
        for row in csv.reader(handler):
            yield row
