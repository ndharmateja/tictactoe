from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/compute", methods=["POST"])
def compute():
    result = {"board": [[0, 0, 1], [0, 1, 0], [1, 0, 0]],
              "isComplete": True, "winner": 1}
    return jsonify(result), 200


if __name__ == "__main__":
    app.run(port=3001, debug=True)
