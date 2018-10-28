from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

counter = 0

@app.route('/counter', methods =['GET'])
def get_counter():
    global counter
    return str(counter), 200

@app.route('/add', methods =['POST'])
def add_1():
    global counter
    counter = counter + 1
    return ''.200

@app.route('/subtract', methods =['POST'])
def add_1():
    global counter
    counter = counter - 1
    return ''.200