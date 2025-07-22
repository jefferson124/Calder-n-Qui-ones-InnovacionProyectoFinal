import copy

def get_best_move(board):
    best_score = float('-inf')
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                board[row][col] = "O"
                score = minimax(board, False)
                board[row][col] = ""
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move

def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == "":
                    board[row][col] = "O"
                    score = minimax(board, False)
                    board[row][col] = ""
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == "":
                    board[row][col] = "X"
                    score = minimax(board, True)
                    board[row][col] = ""
                    best_score = min(score, best_score)
        return best_score

def check_winner(board):
    lines = []

    for i in range(3):
        lines.append(board[i])
        lines.append([board[0][i], board[1][i], board[2][i]])

    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    for line in lines:
        if line[0] != "" and all(cell == line[0] for cell in line):
            return line[0]

    return None

def is_full(board):
    return all(cell != "" for row in board for cell in row)
