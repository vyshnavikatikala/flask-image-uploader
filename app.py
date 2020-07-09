from flask import Flask,render_template,request
from logging import FileHandler,WARNING

app = Flask(__name__,template_folder='template')

file_handler=FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)

app.logger.addHandler(file_handler)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/upload')
def upload():
  file=request.files['inputFile']
  return file.filename 

if __name__=='__main__':
  app.run(debug=True)
