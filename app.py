from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

#client = MongoClient('mongodb:// ~~~ ', 27017)
#db = client.dbjungle

# HTML 화면 보여주기 
@app.route('/')
def home():
    return render_template('index.html')