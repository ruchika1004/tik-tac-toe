import random

def display(board):
    print(f'''
{board[7]}|{board[8]}|{board[9]}                   7| 8| 9
--+--+--                  --+--+--
{board[4]}|{board[5]}|{board[6]}   Positions->     4| 5| 6
--+--+--                  --+--+--
{board[1]}|{board[2]}|{board[3]}                   1| 2| 3
''')

def validInput():
    while True:
        pos=int(input("Enter a position:"))
        if pos in range(1,10):
            return pos
        else:
            print("Not a valid position")

def validpos(turn,board):
    print(f'{turn} chance')
    pos= validInput()
    while True:
        if board[pos]== '  ':
            board[pos]= turn
            break
        else:
            print("Cannot oerwrite. Please select a new loc.")
            pos=validInput()

def checkB(board):
    check=0
    if board[1]==board[2]==board[3] != '  ' or board[4]==board[5]==board[6] != '  ' or board[7]==board[8]==board[9] != '  ':
        check=1
    elif board[1]==board[4]==board[7] != '  ' or board[2]==board[5]==board[8] != '  ' or board[3]==board[6]==board[9] != '  ':
        check=1
    elif board[1]==board[5]==board[9] != '  ' or board[7]==board[5]==board[3] != '  ':
        check=1
    return check


def userinput(board, symbol):
    sym1,sym2=symbol[random.randint(0,1)]
    print(f'{sym1} is going first.\n\n ')
    display(board)
    for i in  range(9):
        if i%2==0:
            turn=' '+sym1
            validpos(turn,board)
        else:
            turn=' '+sym2
            validpos(turn,board)
        display(board)
        if i>=4:
            if checkB(board):
                print(f"'{turn} WON '")
                break
        if i==8:
                print("None won. It's a TIE.")

def main():
    board= ["Just to adjust loc:", '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
    symbol=[('X','O'),('O','X')]
    while True:
        marker=input('\n Enter your marker: ').upper()
        if marker== 'X' or marker== 'O':
            userinput(board, symbol)
        else:
            print("Wrong marker ('X','O'). Please try again.")


if __name__ == "__main__":
    main()
