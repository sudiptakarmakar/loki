from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET", "POST"])
def home():
    return jsonify(message="Hello, world"), 200


@app.route("/ping", methods=["GET", "POST"])
def ping():
    return jsonify(message="PONG"), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
