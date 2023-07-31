# take a 3x3 2d list
# 0 - empty
# 1 - user
# 2 - computer
#
# return a dictionary
# winner - 0 => tie
# winner - 1 => user
# winner - 2 => computer
# {board: [[]], isComplete: true/false, winner: 0/1/2}
def compute_board(board):
  return {"board": [[0, 0, 1], [0, 1, 0], [1, 0, 0]],
              "isComplete": True, "winner": 2}