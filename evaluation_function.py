"""evaluation_function.py
   @author: Josoa ramaroson
   @description: This function aim for determining wether the final board wins or not
   @version: 1.0.0
"""

def evaluate(board: list):
    # Evaluating Row
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            return return_value(board[0][2])
    
    # Evaluating Column
    for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            return return_value(board[0][2])

    # Evaluating left-to-right diagonal
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return return_value(board[0][2])
    
    # Evaluating right-to-left diagonal
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return return_value(board[0][2])
    
    return 0

def return_value(case_value):
        if case_value == "X":
                return 10
        elif case_value == "O":
                return -10