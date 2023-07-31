from flask import Flask, jsonify, request
from flask_cors import CORS
from tictactoe import compute_board


app = Flask(__name__)
CORS(app)


# TODO
# # Validations:
# 1. Every cell should be a number and between 0 and 2
# 2. Number of 1s should be greater than number of 2s by 1
def validate_board(board):
    raise TypeError("")
    pass


@app.route("/compute", methods=["POST"])
def compute():
    board = request.get_json()
    try:
        validate_board(board)
        result = compute_board(board)
        return jsonify(result), 201
    except TypeError as e:
        return jsonify({"error": str(e)}), 401
    except:
        return jsonify({"error": "Unknown error"}), 500



if __name__ == "__main__":
    app.run(port=3001, debug=True)
