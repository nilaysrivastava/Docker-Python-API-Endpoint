from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(message="Hello, World!")

@app.route('/info')
def info():
    return jsonify(info="This is a simple Flask API endpoint.")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
