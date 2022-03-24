from flask import jsonify, render_template, request
from app import app


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
    print(request)
