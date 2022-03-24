from calendar import c
from urllib import response
from flask import jsonify, render_template, request
from app import app
from parabola import main_parabola
import base64
import os
from time import sleep

# Headers
@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

# Main page
@app.route("/")
def home():
    return render_template("index.html")

### Math ###
@app.route("/parabola", methods=['POST'])
def parabola():
    sleep(3)
    var = request.json['variables']
    
    main_parabola(a=var['a'], b=var['b'], c=var['c'])

    with open('./calc_img/parabola.png', 'rb') as imf: 
        encoded_string = base64.b64encode(imf.read())

    return encoded_string
