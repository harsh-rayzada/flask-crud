from flask import Flask, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/flaskfiletest'
mongo = PyMongo(app)

@app.route('/')
def home():
    return '''
        <form method='POST' action='/create' enctype='multipart/form-data'>
            <input type='file' name='myfile'>
            <input type='Submit'>
        </form>
    '''

@app.route('/create', methods=['POST'])
def create():
    if 'myfile' in request.files:
        imageFile = request.files['myfile']
        mongo.save_file(imageFile.filename, request.files['myfile'])
        return 'uploaded!'
    else:
        return 'no file found'

@app.route('/file/<filename>', methods=['GET'])
def getfile(filename):
    return mongo.send_file(filename)
