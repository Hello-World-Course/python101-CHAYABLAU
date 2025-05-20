# THIS CODE IS WRONG, FIX IT AND ADD NEW CODE
name =None
board_size =None
number_of_mines= None
name = input("Hello, whats your name")
if(len(name)<2):
    print("Your name is too short")
    name=None

else:
    board_size = int(input(f"{name}, please choose board size"))
    if( board_size<=0 or board_size>=26):
       print(f"{name}, you have entered illegal board size")
       board_size=None
       number_of_mines=None
    else:
        number_of_mines= int(input(f"{name}, for board size {board_size}, choose number of mines to allocate"))
        if(number_of_mines>(board_size * board_size) /2 or number_of_mines<=0):
           print(f"{name}, you have entered illegal number of mines")
           number_of_mines=None
        else:print(f"{name}, the board size is: {board_size} ,the number of mines is: {number_of_mines}. ENJOY!")
