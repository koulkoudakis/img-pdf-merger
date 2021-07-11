import sys
import os
import img2pdf
# import PyPDF2


pdfName = sys.argv[1]
# inputs = sys.argv[2:]
imgDir = "./images"

# check if imgDir exists, and if not, create

if not os.path.exists(imgDir):
  os.makedirs(imgDir)

# convert all files ending in .jpg or .png inside a directory

imgs = []
for fname in os.listdir(imgDir):
	if not fname.endswith((".jpg", ".png")):
		continue
	path = os.path.join(imgDir, fname)
	if os.path.isdir(path):
		continue
	imgs.append(path)

print('Converting images to .pdf...')

with open("merged-pdf.pdf","wb") as f:
	f.write(img2pdf.convert(imgs))

print(f'.pdf {pdfName}.pdf created')

# def pdf_combiner(pdf_list):
#   merger = PyPDF2.PdfFileMerger()
#   for pdf in pdf_list:
#     merger.append(pdf)
#     print(pdf)
#   merger.write(f'{pdfName}.pdf')

# with open('pdf-1.pdf', 'rb') as pdf:
#   reader = PyPDF2.PdfFileReader(pdf)
#   page = reader.getPage(0)
#   page.rotateCounterClockwise(90)
#   writer = PyPDF2.PdfFileWriter()
#   writer.addPage(page)
#   with open('tilt.pdf', 'wb') as new_pdf:
#     writer.write(new_pdf)

# pdf_combiner(inputs)