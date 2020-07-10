from flask import Flask,render_template,request
import os,glob

f=open('image.txt','r')
g= f.read()

app= Flask(__name__,template_folder='template')
@app.route('/')
def index():
    return render_template('index.html',n=g)

if __name__=="__main__":
    app.run(debug=True)