import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    message = "Hello, World!"
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run()
