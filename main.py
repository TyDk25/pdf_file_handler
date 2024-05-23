from docx2pdf import convert
from pdf2docx import Converter
from pathlib import Path


def pdf_to_word(pdf_file) -> None:
    """
    :param pdf_file: filepath of where .pdf file is located
    :return: None
    """
    file_path = Path(pdf_file)
    destination_dir = file_path.parent
    name_of_pdf = file_path.stem + '.docx'
    output = destination_dir / name_of_pdf
    cv = Converter(pdf_file)
    cv.convert(str(output))


def convert_word_to_pdf(filepath) -> None:
    """
    :param filepath: filepath of where .docx file is located
    :return: None
    """
    file_path = Path(filepath)
    destination_dir = file_path.parent
    name_of_pdf = file_path.stem + '.pdf'
    output = destination_dir / name_of_pdf
    convert(filepath, output)



