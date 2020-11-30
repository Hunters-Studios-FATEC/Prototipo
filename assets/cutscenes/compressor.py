from zipfile import ZipFile
import os


def compress():
    with ZipFile('cutscenes.zip', 'w') as zipobj:
        for i in range(25):
            zipobj.write(f'cut{i + 1}.json')
            os.remove(f'cut{i + 1}.json')


def decompress():
    with ZipFile('assets/cutscenes/cutscenes.zip', 'r') as zipobj:
        zipobj.extractall('assets/cutscenes')
    os.remove('assets/cutscenes/cutscenes.zip')
