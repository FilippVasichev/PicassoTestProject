import os
from transliterate import translit

def filename_to_ascii(filename: str) -> str:
    return filename if filename.isascii() else translit(filename, reversed=True)
