from PyPDF4 import PdfFileReader, PdfFileWriter
from PyPDF4.pdf import ContentStream
from PyPDF4.generic import TextStringObject, NameObject
from PyPDF4.utils import b_

def remove_watermark(wm_text, inputFile, outputFile):
    with open(inputFile, "rb") as f:
        source = PdfFileReader(f, "rb")
        output = PdfFileWriter()

        for page in range(source.getNumPages()):
            page = source.getPage(page)
            content_object = page["/Contents"].getObject()
            content = ContentStream(content_object, source)

            for operands, operator in content.operations:
                if operator == b_("Tj"):
                    text = operands[0]

                    if isinstance(text, str) and text.startswith(wm_text):
                        operands[0] = TextStringObject('')

            page.__setitem__(NameObject('/Contents'), content)
            output.addPage(page)

        with open(outputFile, "wb") as outputStream:
            output.write(outputStream)
            
wm_text = 'Goldenagato | mp4directs.com'
inputFile = r'C:\Users\Admin\Downloads\Bottom-Tier Character Tomozaki, Vol. 8.5_unlocked.pdf'
outputFile = r"C:\Users\Admin\Downloads\Bottom-Tier Character Tomozaki, Vol. 8.5 - Clocker.pdf"
remove_watermark(wm_text, inputFile, outputFile)