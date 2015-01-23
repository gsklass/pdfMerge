# Merge back PDFs
import sys
from pyPdf import PdfFileReader, PdfFileWriter
 
"""
The code currently expects the first argument to be the 
'base name' of the PDF files. Implied is that there are 
two files 1) the <base name> + " (front).pdf" that contains
the odd pages and 2) <base name> + " (back).pdf" that 
contains the (reverse ordered) even pages. The result
will be a file called <base name>+".pdf" that is the 
merged PDF file.
"""
baseFile = "2014 Encompass Auto Policy Info"
baseFile = sys.argv[1]
backFile = baseFile  + " (back).pdf"
frontFile = baseFile +" (front).pdf"

output = PdfFileWriter()
try:
  pdfFrnt = PdfFileReader(file( frontFile, "rb"))
except:  
  frontFile = baseFile +" (Front).pdf"
  pdfFrnt = PdfFileReader(file( frontFile, "rb"))

try:
  pdfBack = PdfFileReader(file( backFile, "rb"))
except:  
  backFile = baseFile  + " (Back).pdf"
  pdfBack = PdfFileReader(file( backFile, "rb"))

  
frntCount = pdfFrnt.getNumPages()
backCount = pdfBack.getNumPages()

if frntCount == backCount:
  print "We're going to merge"
  for page in range(frntCount):
    output.addPage(pdfFrnt.getPage(page))
    #print page
    output.addPage(pdfBack.getPage(backCount-page-1))
    #print backCount-page-1
else:
  print "Can't merge"
   
outputStream = file(baseFile +".pdf", "wb")
output.write(outputStream)
outputStream.close()

