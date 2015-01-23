# Merge back PDFs
import sys
from pyPdf import PdfFileReader, PdfFileWriter
 
"""
2014-08 Ford Transmission Recall (Back).pdf
2014-09 Novetta Escrow (JPMC) (Back).pdf
2014-10-02 Encompass Auto Insurance (Back).pdf
2014-10-29 Encompass Insurance (Back).pdf
2014-11 JPMorgan Chase escrow statement (back).pdf
2014-12-09 Experian Credit Report (back).pdf
2014-12-29 IRS PIN (back).pdf
2014-12-30 Sprint AIRAVE aggrement (back).pdf
2014-12-31 Experian Credit Report Correction (back).pdf
2014 Encompass Delux Home Policy (Back).pdf
2014-Q3 DAF Statement (Back).pdf
baseFile = "1999-02-03 Letter from Lindsey"
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

