#it turns indices from a dict to number of a 2D list.         
def get_indices_from_number(number):
    return int(number/3), number % 3


def check_winner(board, n):
    combinations = [[0,3,6], [1,4,7], [2,5,8],[0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6], [0,1,2], [3,4,5], [6,7,8]]
    for combination in combinations:
        for number in combination:
            i, j = get_indices_from_number(number)
            if board[i][j] != n: break
        else: return True
    return False


def check_tie(board):
    for lst in board:
        if 0 in lst: break
    else: return True
    return False



# to check if computer is one step close to winning
def check_winning(board):
    combinations = [[0,3,6], [1,4,7], [2,5,8],[0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6], [0,1,2], [3,4,5], [6,7,8]]
    count = 0
    
    for combination in combinations:
        for number in combination:
            i, j = get_indices_from_number(number)
            if board[i][j] == 2:
                count += 1
            if board[i][j] == 1: break
        else:
            if count == 2:
                for number in combination:
                    i, j = get_indices_from_number(number)
                    if board[i][j] == 0: return number
        count = 0
    return False

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


