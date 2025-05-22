# THIS CODE IS WRONG, FIX IT AND ADD NEW CODE

def is_name_valid(name):
    if len(name) >2:
        return True
    return False
def is_board_size_valid(board_size):
    if board_size >0 and board_size < 26:
        return True
    return False
def is_number_of_mines_valid( board_size,number_of_mines):
    if number_of_mines <board_size*board_size/2:
        return True
    return False
def register_user():
    name = input("Hello, whats your name")
    if (is_name_valid(name)==False):
        print("Your name is too short")
        return None,None,None
    else:
        board_size = int(input(f"{name}, please choose board size"))
        if (is_board_size_valid(board_size)==False):
            print(f"{name}, you have entered illegal board size")
            return None, None, None
        else:
            number_of_mines = int(input(f"{name}, for board size {board_size}, choose number of mines to allocate"))
            if (is_number_of_mines_valid(board_size,number_of_mines)==False):
                print(f"{name}, you have entered illegal number of mines")
                return None, None, None
            else:
                return name,board_size,number_of_mines


#user_name, user_board_size, user_num_mines = register_user()
#print(f"name:{user_name}, board size:{user_board_size}, number of mines:{user_num_mines}")
