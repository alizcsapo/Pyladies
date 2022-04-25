board = 20*"-"
print(board)
evaluate = "-"
while evaluate == "-":
#def player_move (position):
    position = int(input("Where do you want to place your mark next?(1-20):"))
    #if position >20 :
    while position >20  :
            position = int(input("Please insert a valid mark?(1-20):"))
    while board[position-1]!="-"  :
            position = int(input("Postion already taken?(1-20):"))
    if board[position-1]=="-" :
            board = board[:position-1] + "X" + board[position:] # Here I combine the ---- and the mark in the given position (position is altered to reflect the Player choice numbering and not python numbering)
#    else: 
 #           position = int(input("Please choose an empty position:"))
  #          board = board[:position-1] + "X" + board[position:]
            #return
    print(board)
    from random import randrange
    #def computer_move (positioncomputer):
    #positioncomputer = randrange(19)
    position = randrange(19)
    while board[position]!="-" :
        position = randrange(19)
    if board[position]=="-":
    #if board[position]=="-":
        #board = board[:position] + "O" + board[position+1:]
       board = board[:position] + "O" + board[position+1:]
    #else:
     #   positioncomputer = randrange(19)
      #  board = board[:positioncomputer] + "O" + board[positioncomputer+1:]
    print(board)
    if "XXX" in board:
        evaluate = "X"
        print("X")
        break
    elif "OOO" in board:
        evaluate = "O"
        print("O")
        break
    elif "-" in board:
        evaluate = "-"
        print("-")
else: print("!")