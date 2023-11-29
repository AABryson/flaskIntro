from flask import Flask, request
from operations import add, sub, mult, div #need to work on this; forgot to import each function
 
app = Flask(__name__)

@app.route('/add') #don't hardcode math oepration in route functions; use operations.py
def do_add(): #don't call operation function here
    a = int(request.args.get("a")) #review
    b = int(request.args.get("b"))
    result = add(a, b)
    return str(result)

@app.route("/sub")
def do_sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)
    return str(result)

@app.route("/mult")
def do_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)
    return str(result)

@app.route("/div")
def do_div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)
    return str(result)

