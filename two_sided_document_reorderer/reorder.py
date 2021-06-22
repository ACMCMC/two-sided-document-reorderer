from enum import Enum
import PyPDF2
from PyPDF2.pdf import PdfFileReader


class Mode(Enum):
    """
    The modes available for performing the reorder
    """
    STANDARD = 0
    REVERSE_SECOND = 1


def reorder(pdf1: PdfFileReader, pdf2: PdfFileReader) -> PyPDF2.PdfFileWriter:
    """
    Takes two PDF files (as PdfFileReader objects), and merges their pages in a common PdfFileWriter, according to the following scheme:
    [PDF 1, page 1] [PDF 2, page 1] [PDF 1, page 2] [PDF 2, page 2] ... [PDF 1, page P] [PDF 2, page P]
    """
    pdfWriter = PyPDF2.PdfFileWriter()

    if not (pdf1.getNumPages() == pdf2.getNumPages()) or ((pdf1.getNumPages() - 1) == pdf2.getNumPages()):
        raise ValueError('The number of pages of both PDFs should be the same (or differ in an unit, with the first PDF having the greater value). The first one has {0} pages, and the second one has {1} pages.'.format(
            pdf1.getNumPages(), pdf2.getNumPages()))

    # We use pdf2.getNumPages() because it's the lesser of the two values
    for i in range(pdf2.getNumPages()):
        pdfWriter.addPage(pdf1.getPage(i))
        pdfWriter.addPage(pdf2.getPage(i))

    if (pdf1.getNumPages() - 1) == pdf2.getNumPages():
        pdfWriter.addPage(pdf1.getPage(pdf1.getNumPages()-1))

    return pdfWriter


def reorder_reverse(pdf1: PdfFileReader, pdf2: PdfFileReader) -> PyPDF2.PdfFileWriter:
    """
    Takes two PDF files (as PdfFileReader objects), and merges their pages in a common PdfFileWriter, according to the following scheme:
    [PDF 1, page 1] [PDF 2, page P] [PDF 1, page 2] [PDF 2, page P-1] ... [PDF 1, page P] [PDF 2, page 1]
    As can be seen, the second PDF is added in reverse order.
    """
    pdfWriter = PyPDF2.PdfFileWriter()

    if not (pdf1.getNumPages() == pdf2.getNumPages()) or ((pdf1.getNumPages() - 1) == pdf2.getNumPages()):
        raise ValueError('The number of pages of both PDFs should be the same (or differ in an unit, with the first PDF having the greater value). The first one has {0} pages, and the second one has {1} pages.'.format(
            pdf1.getNumPages(), pdf2.getNumPages()))

    # We use pdf2.getNumPages() because it's the lesser of the two values
    for i in range(pdf2.getNumPages()):
        pdfWriter.addPage(pdf1.getPage(i))
        pdfWriter.addPage(pdf2.getPage(pdf2.getNumPages() - i))

    if (pdf1.getNumPages() - 1) == pdf2.getNumPages():
        pdfWriter.addPage(pdf1.getPage(pdf1.getNumPages()-1))

    return pdfWriter


def run(pdf1_path, pdf2_path, output_path, **kwargs):
    """
    Takes the input paths of two PDF files and merges them according to the logic defined in reorder(), outputting the result to the output_path.
    """
    with open(pdf1_path, 'rb') as f1, open(pdf2_path, 'rb') as f2, open(output_path, 'wb') as f_out:
        pdf1 = PdfFileReader(f1)
        pdf2 = PdfFileReader(f2)
        if kwargs.get('mode') == Mode.REVERSE_SECOND:
            output_pdf = reorder_reverse(pdf1, pdf2)
        else:
            output_pdf = reorder(pdf1, pdf2)
        output_pdf.write(f_out)
