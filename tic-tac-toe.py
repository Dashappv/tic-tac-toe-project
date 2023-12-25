from random import randrange
board = str('-' * 20)

# step 1
def evaluate(board):
    if 'xxx' in board:
        return 'x won'
    elif 'ooo' in board:
        return 'o won'
    elif '-' not in board:
        return '!'
    else:
        return '-'

# step 2
def move(board, mark, position):
    updated_board = board[:position] + mark + board[position + 1: ]
    return updated_board

# step 3
def player_move(board):
    position = int(input("What position you wanna play?"))
    while 0 > position or position > 19 or board[position] == "o":
        print("Please choose another spot")
        position = int(input("What position you wanna play?"))
    return move (board, "x", position)

# step 4
def pc_move(board):
    position = randrange(20)
    while board[position] == 'x':
        position = randrange(20)
    return move (board, "o", position)

# step 5
def full_game(board):
    while True:
        print(board)

        board = player_move(board)
        print(board)
        outcome_move = evaluate(board)
        if outcome_move != '-':
            print(outcome_move)
            break

        board = pc_move(board)
        print(board)
        outcome_move = evaluate(board)
        if outcome_move != '-':
            print(outcome_move)
            break
full_game(board)