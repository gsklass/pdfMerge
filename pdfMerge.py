# Merge back PDFs
import sys
 
"""
The code currently expects the first argument to be the 
'base name' of the PDF files. Implied is that there are 
two files 1) the <base name> + " (front).pdf" that contains
the odd pages and 2) <base name> + " (back).pdf" that 
contains the (reverse ordered) even pages. The result
will be a file called <base name>+".pdf" that is the 
merged PDF file.
baseFile = "2014 Encompass Auto Policy Info"
baseFile = sys.argv[1]
backFile = baseFile  + " (back).pdf"
frontFile = baseFile +" (front).pdf"
"""

def baseNameToNamingConvention(baseName):
  frontFile = baseName +" (front).pdf"
  try:
    file (frontFile, "rb")
  except:  
    frontFile = baseName +" (Front).pdf"

  try:
    file( frontFile, "rb")
  except:
    print "no corresponding front file"
    return "","",""

  backFile = baseName +" (back).pdf"
  try:
    file (backFile, "rb")
  except:  
    backFile = baseName +" (Back).pdf"

  try:
    file(backFile, "rb")
  except:
    print "no corresponding back file"
    return "","",""

  resultsFile = baseName +".pdf"
  try:
    aFile = file(resultsFile,"wb")
  except:
    print "problems opening results file"
    return "","",""
  aFile.close()
  print frontFile,backFile,resultsFile
  return frontFile,backFile,resultsFile

def pdfMerger(frontFileName, backFileName, resultsFileName):
  from pyPdf import PdfFileReader, PdfFileWriter

  pdfFrnt = PdfFileReader(file( frontFileName, "rb"))
  pdfBack = PdfFileReader(file( backFileName, "rb"))
  
  frntCount = pdfFrnt.getNumPages()
  backCount = pdfBack.getNumPages()

  if frntCount == backCount:
    pdfResults = file(resultsFileName, "wb")
    output = PdfFileWriter()
    for page in range(frntCount):
      output.addPage(pdfFrnt.getPage(page))
      output.addPage(pdfBack.getPage(backCount-page-1))
    output.write(pdfResults)
    pdfResults.close()
    return 2*frntCount
  else:
    print "page count mismatch: Can't merge"
    return 0

if __name__ == "__main__":
  baseName = sys.argv[1]
  frontName,backName,resultName = baseNameToNamingConvention(baseName)
  pdfMerger(frontName,backName,resultName)
