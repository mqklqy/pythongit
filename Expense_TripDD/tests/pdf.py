from PyPDF2 import PdfFileWriter, PdfFileReader


def extrac_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
    return information


def rotate_page(pdf_path):
    pdf_reader = PdfFileReader(pdf_path)
    pdf_writer = PdfFileWriter()
    page1 = pdf_reader.getPage(0)
    # page1 = page1.roateCounterClockwise(90)#逆时针旋转
    page1 = page1.roateClockwise(90)  # 顺时针旋转
    pdf_writer.addPage(page1)

    with open('rotate_pdf.pdf', 'wb') as fp:
        pdf_writer.write(fp)


if __name__ == '__main__':
    information = extrac_information('test.pdf')
    print(information)
