def is_on_board(x, y, board):
    # This is wrong fix it:
    if len(board) > x >0 and len(board) > y>0:
        return True
    return False

def safe_set_value( x, y, value, board):
    if is_on_board(x, y, board):
        board[x][y] = value
        return True
    return False
