import sys, os
from flask import Flask, jsonify, request
from flask_cors import CORS
import git


# to not generate pycache (this line before local imports)
sys.dont_write_bytecode = True


# local imports
from tictactoe import compute_board


app = Flask(__name__)
CORS(app)


# # Validations:
# 1. Every cell should be a number and between 0 and 2
# 2. Number of 1s should be greater than number of 2s by 1
def validate_board(board):
    if type(board) != list:
        raise TypeError("board should be a list")
    if len(board) != 3:
        raise TypeError("board needs to have 3 rows")
    for row in board:
        if len(row) != 3:
            raise TypeError("each row in board needs to have 3 elements")

    num_ones = 0
    num_twos = 0
    for row in board:
        for number in row:
            if type(number) != int:
                raise TypeError("each element needs to be an integer")
            if number < 0 or number > 2:
                raise TypeError("each element needs to be an integer")
            if number == 1:
                num_ones += 1
            elif number == 2:
                num_twos += 1

    if num_ones - num_twos != 1:
        raise TypeError("invalid number of ones and twos")


@app.route("/compute", methods=["POST"])
def compute():
    board = request.get_json()
    try:
        validate_board(board)
        result = compute_board(board)
        return jsonify(result), 201
    except TypeError as e:
        print("Validation Error: " + str(e))
        print(board)
        return jsonify({"error": str(e)}), 401
    except Exception as e:
        print("Error: " + str(e))
        print(board)
        return jsonify({"error": "Unknown error"}), 500
    

# Webhook
@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('path/to/git_repo')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400


if __name__ == "__main__":
    app.run(port=os.environ.get("PORT", 3001), debug=False, host='0.0.0.0')
