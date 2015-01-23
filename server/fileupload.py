import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename
import traceback
import sys
from pyPdf import PdfFileReader, PdfFileWriter

UPLOAD_FOLDER = './'
ALLOWED_EXTENSIONS = set(['pdf'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        frontFile = request.files['frontFile']
        backFile = request.files['backFile']
        filename = request.form['filename']
        if frontFile and allowed_file(frontFile.filename) and backFile and allowed_file(backFile.filename):
            #filename = secure_filename(file1.filename)
            #file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            output = PdfFileWriter()
            try:
                pdfFrnt = PdfFileReader(frontFile)
            except:  
                #frontFile = baseFile +" (Front).pdf"
                pdfFrnt = PdfFileReader(frontFile)

            try:
                pdfBack = PdfFileReader(backFile)
            except:  
                #backFile = baseFile  + " (Back).pdf"
                pdfBack = PdfFileReader(backFile)


            frntCount = pdfFrnt.getNumPages()
            backCount = pdfBack.getNumPages()

            if frntCount == backCount:
                #print "We're going to merge"
                for page in range(frntCount):
                    output.addPage(pdfFrnt.getPage(page))
                    #print page
                    output.addPage(pdfBack.getPage(backCount-page-1))
                    #print backCount-page-1
            else:
                return "Can't merge"

            outputStream = file(UPLOAD_FOLDER + filename +".pdf", "wb")
            output.write(outputStream)
            outputStream.close()
            return "upload successful"
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method='post' enctype='multipart/form-data'>
      <p><input type='text' name='filename'></p>
      <p><input type='file' name='frontFile'></p>
        <p><input type='file' name='backFile'>
         <input type='submit' value='Upload'></p> 
    </form>
    '''


if __name__ == "__main__":
    app.debug = True
    app.run()
    