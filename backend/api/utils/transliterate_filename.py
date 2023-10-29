from transliterate import translit


def filename_to_ascii(filename: str) -> str:
    """
    Транслитерирует имена загружаемых файлов с кириллицы в латиницу.
    """
    return filename if filename.isascii() else translit(
        filename, reversed=True
    )
