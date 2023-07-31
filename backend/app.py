from flask import Flask, jsonify, request
from flask_cors import CORS
from tictactoe import compute_board


app = Flask(__name__)
CORS(app)


@app.route("/compute", methods=["POST"])
def compute():
    board = request.get_json()
    result = compute_board(board)
    return jsonify(result), 201


if __name__ == "__main__":
    app.run(port=3001, debug=True)
