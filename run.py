import datetime
from flask import Flask, render_template, jsonify, request
from controler import *
app = Flask(__name__)

@app.route('/admin/', methods = ["GET", "POST"])
def admin():
	return "aqui sera a area de administracao"


@app.route('/events/')
@app.route('/events/<path:event>')
def events(event = None):
	
	if event:
		return "event" + event
	
	return "aqui ficarao os eventos"

@app.route('/', methods = ["GET", "POST"])
def index():
	return "aqui ficara a main page com acesso ao admin"

@app.route('/about')
def about():
	return "projeto open source construido pela galera ai"

if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0")

