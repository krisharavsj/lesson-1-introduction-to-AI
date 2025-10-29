import random
from colorama import init,Fore,Style
def display_board(board):
    print()
    def colored(cell):
        if cell=='X':
            return Fore.RED+ cell + Style.RESET_ALL
        elif cell=='O':
            return Fore.BLUE+ cell + Style.RESET_ALL
        else:
            return Fore.YELLOW+ cell + Style.RESET_ALL
    print(' '+ colored(board[0])+'|'+colored(board[1])+'|'+colored(board[2]))
    print(Fore.CYAN+'------------'+Style.RESET_ALL)
    print(' '+ colored(board[3])+'|'+colored(board[4])+'|'+colored(board[5]))
    print(Fore.CYAN+'------------'+Style.RESET_ALL)
    print(' '+ colored(board[6])+'|'+colored(board[7])+'|'+colored(board[8]))
    print()

def player_choice():
    symbol=''
    while symbol not in ['X','O']:
        symbol=input(Fore.GREEN+"do you want to be 'X'or'O'?"+Style.RESET_ALL).upper()
    if symbol=='X':
        return 'X','O'
    else:
        return 'O','X'

def player_move(board,symbol):
    move=-1
    while move not in range(0,9) or not board[move - 1].isdigit():
        try:
            move=int(input("Enter your move (0-8) "))
            if move not in range(0,9)or board[move - 1].isdigit():
                print("Invalid move please try again")
        except ValueError:
            print("please enter a number between 0 and 8")
    board[move - 1]=symbol
