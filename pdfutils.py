
import sys, fitz

path = "clock.pdf"

doc = fitz.open(path)  # open document
out = open(path + ".txt", "wb")  # open text output
for page in doc:  # iterate the document pages
    text = page.get_text().encode("utf8")  # get plain text (is in UTF-8)
    out.write(text)  # write text of page
    out.write(bytes((12,)))  # write page delimiter (form feed 0x0C)
out.close()


print(text)
# with open("output.txt", "w", encoding="utf-8") as f:
#         f.write(text)



# from PyPDF4 import PdfFileReader

# def extract_information(pdf_path):
#     with open(pdf_path, 'rb') as f:
#         pdf = PdfFileReader(f)
#         information = pdf.getDocumentInfo()
#         number_of_pages = pdf.getNumPages()

#         with open("output.txt", "w", encoding="utf-8") as f:
#             for i in range(0, number_of_pages):
#                 page = pdf.getPage(i)
#                 page_content = page.extractText()
#                 page_content.encode('utf-8')
#                 f.write(page_content)

#     # txt = f"""
#     # Information about {pdf_path}: 

#     # Author: {information.author}
#     # Creator: {information.creator}
#     # Producer: {information.producer}
#     # Subject: {information.subject}z
#     # Title: {information.title}
#     # Number of pages: {number_of_pages}
#     # """

#     # print(information)
#     return information

# if __name__ == '__main__':
#     path = 'clock.pdf'
#     extract_information(path)