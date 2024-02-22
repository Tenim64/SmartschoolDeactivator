from flask import Flask, render_template, request
from deactivater import *
import time
app = Flask(__name__)


@app.route('/output', methods=['POST'])
def output():
   try:
      deactivate(request.form['smartschooladres'], request.form['gebruikersnaam'])
      return render_template('./succes.html')
   except:
      return render_template('./failed.html')
    
   
@app.route('/')
def home():
   return render_template('./index.html')

@app.route('/voorwaarden')
def voorwaarden():
   return render_template('./voorwaarden.html')

if __name__ == '__main__':
   app.run("0.0.0.0", 80, debug=True)