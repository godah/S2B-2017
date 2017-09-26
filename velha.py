import os

def initBoard():
    board = [" "," "," "," "," "," "," "," "," "]
    os.system('clear')
    print("S2B-2017 Tic Tac Toe!\n")
    print(" 7 | 8 | 9")
    print(" --+---+--")
    print(" 4 | 5 | 6")
    print(" --+---+--")
    print(" 1 | 2 | 3")  
    print("\n\n")
    return board

def showBoard(board):
    os.system('clear')
    print("S2B-2017 Tic Tac Toe!\n")
    print(" {b[6]} | {b[7]} | {b[8]}".format(b = board))
    print(" --+---+--")
    print(" {b[3]} | {b[4]} | {b[5]}".format(b = board))
    print(" --+---+--")
    print(" {b[0]} | {b[1]} | {b[2]}".format(b = board))
    print("\n\n")

def turn(mark,board):
    flag = False
    while not flag:
        requestTurn(mark)
        pos = input()
        if pos.isnumeric():
            pos = int(pos) - 1
            if pos >= 0 and pos <= 8 and board[pos] == " ":
                board[pos] = mark
                flag = True
        showBoard(board)   
    mark = swapTurn(mark)  
    return mark, board
    
def requestTurn(mark):
    if mark == "\033[92mX\033[0m":
        print("Player1 (\033[92mX\033[0m) make your choice:")
    else:
        print("Player2 (\033[91mO\033[0m) make your choice:")    

def swapTurn(mark):
    if mark == "\033[92mX\033[0m":
        return "\033[91mO\033[0m"
    else:
        return "\033[92mX\033[0m"

def tied(board):
    i = 0
    while i < 9:
        if board[i] == " ":
            return False
        i = i + 1
    print("Draw!")
    return True

def checkColumn(board):
    for i in range(3):
        if board[i] != " " and (board[i] == board[i+3] and board[i+3] == board[i+6]):
            return True
    return False

def checkLine(board):
    for i in range(7):
        if i%3 == 0:
            if board[i] != " " and (board[i] == board[i+1] and board[i+1] == board[i+2]):
                return True
    return False

def checkDiagonal(board):
    if board[4] != " " and ((board[0] == board[4] and board[4] == board[8]) or (board[2] == board[4] and board[4] == board[6])):
        return True
    return False

def won(board):
    if checkDiagonal(board) or checkLine(board) or checkColumn(board):
        return True
    else:
        return False
    
def finish(mark):
    if mark != "\033[92mX\033[0m":
        print("Player1 Won!")
    else:
        print("Player2 Won!")
    

def main():
    mark = "\033[92mX\033[0m"
    end = False
    board = initBoard()
   
    while not end:
        mark, board = turn(mark, board)  
        if won(board):
            finish(mark)
            end = True
        else:
            end = tied(board)
      
    print("Play Again?(s)")
    again = input()
    if again == "s" or again == "":  
        main()
    else:
        print("Thanks, see you later!")
            
main()
