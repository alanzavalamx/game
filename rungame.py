#!/usr/bin/env python3.7
import random
from os import system
import platform
import time

"""
A Tic Tac Toe game implementation.

Author: Alan Alexis Zavala Mendoza
Date: July, 2020.

License: GNU GENERAL PUBLIC LICENSE (GPL)
"""


def winnerWays(pass_movements):
    """
    Test to look if someone wins.    
    """
    for subset in winPos:
        count = 0
        for movements in pass_movements:
            if movements in subset:
                count += 1
        if count == 3:
            return True
    return False

def winner(ai_pass,person_pass, ai_choice, h_choice):
    """
    Returns if someone wins to finish the game.
    """
    if winnerWays(ai_pass):
        clean()
        print('SORRY, MR. ROBOT WINS!')
        render_board(ai_pass, person_pass, ai_choice, h_choice)
        return True
    if winnerWays(person_pass):
        clean()
        print('CONGRATULATIONS, YOU WINS!')
        render_board(ai_pass, person_pass, ai_choice, h_choice)
        return True
    
    return False

def isInWinWays(an_pass):
    """
    Test if Ai or Human have posibilitis to win in the next move.
    """
    maybe_win = []

    for subset in winPos:
        count = 0
        sub_maybe = set()
        for movement in an_pass:
            if movement in subset:
                sub_maybe.add(movement)
                count += 1
        if count == 2:
            value = next(iter(set(subset) - sub_maybe) )
            if value in table_board:
                maybe_win.append(value)

    return maybe_win

def theyNeverWins(ai_pass,person_pass):
    """
    Return Ai and Human posibilities to win.
    """
    maybe_win_ai = isInWinWays(ai_pass)
    maybe_win_person = isInWinWays(person_pass)

    return maybe_win_ai, maybe_win_person

def AiChoose(ai_pass, person_pass):
    """
    Returns Ai choose, 
    Test fist if Ai have posibilities to win to choose that choice, 
    if not but Human have posibilities to win, choose the choice to block it, 
    else choose random available position.
    """

    time.sleep(2)

    mov_list = []
    ai_win, blok_person = theyNeverWins(ai_pass,person_pass)

    if len(ai_win) > 0:
        n = next(iter(ai_win))
        return n

    if len(blok_person) > 0:
        n = next(iter(blok_person))
        return n
    

    #TRY TO WIN CENTER
    if 5 in table_board:
        return 5
    
    #UNCOMMENT THIS SECTION IF WANT TO HAVE A UNBEATABLE AI
    #count = 0
    #for i in person_pass:
    #    if i in [1,3,7,9]:
    #        count += 1
    #    if count > 1:
    #        for x in table_board:
    #            if x in [2,4,6,8]:
    #                return x

    #CORNERS CHOOSE
    for i in table_board:
        if i in [1,3,7,9]:
            mov_list.append(i)
        if len(mov_list) > 0:
            n = random.choice(mov_list)
            return n

    #SECOND CENTERS CHOOSE 
    for i in table_board:
        if i in [2,4,6,8]:
            mov_list.append(i)
        if len(mov_list) > 0:
            n = random.choice(mov_list)
            return n

def badChoose(pos_selected):
    """
    Test if Human or Ai choose is allowed.
    """
    error = False
    if (pos_selected >= 1) and (pos_selected <= 9):
        if pos_selected in table_board:
           table_board.remove(pos_selected)
        else:
            error = True
    else:
        error = True
    return error

def render_board(ai_pass, person_pass, ai_choice, h_choice):
    """
    Print the current board on console
    """
    cboard =[]
    board = [1,2,3,4,5,6,7,8,9]

    for cell in board:
        if cell in ai_pass:
            cboard.append(ai_choice)
        elif cell in person_pass:
            cboard.append(h_choice)
        else:
            cboard.append(' ')

    f_line = '-'
    int_cell ='||               '

    print('\n' + f_line * 53)
    print( int_cell * 4)
    print(f'||       {cboard[0]}       ||       {cboard[1]}       ||       {cboard[2]}       ||')
    print( int_cell * 4)
    print(f_line * 53)
    print( int_cell * 4)
    print(f'||       {cboard[3]}       ||       {cboard[4]}       ||       {cboard[5]}       ||')
    print( int_cell * 4)
    print(f_line * 53)
    print( int_cell * 4)
    print(f'||       {cboard[6]}       ||       {cboard[7]}       ||       {cboard[8]}       ||')
    print( int_cell * 4)
    print(f_line * 53)

def clean():
    """
    Clears the bash console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')

    print('Tic Tac Toe Game!\n\n')

def playgame(ai_choice, h_choice, username):
    """
    Function whitch run the game.
    """

    global table_board
    table_board = set([1,2,3,4,5,6,7,8,9])
    ai_start = whoStart()
    ai_pass = set()
    person_pass = set()

    #GAME STARTS
    while len(table_board) > 0:

        clean()
        
        if ai_start:
            print(f'Current player: Mr. Robot, ( {ai_choice} )')
            render_board(ai_pass, person_pass, ai_choice, h_choice)
            pos_selected = AiChoose(ai_pass, person_pass)
            error = badChoose(pos_selected)
            if not error:
                ai_pass.add(pos_selected)
                ai_start = False
            else:
                break
        else:
            print(f'Current player: {username}, ( {h_choice} )')
            render_board(ai_pass, person_pass, ai_choice, h_choice)
            try:
                pos_selected = int(input('Select a empty cell (1-9): '))
                if pos_selected:
                    error = badChoose(pos_selected)
                    if not error:
                        person_pass.add(pos_selected)
                        ai_start = True
            except:
                pass

        if winner(ai_pass,person_pass, ai_choice, h_choice):
            playNewGame(ai_choice, h_choice, username)

        if len(table_board) == 0:
            clean()
            print('                        DRAW!')
            render_board(ai_pass, person_pass, ai_choice, h_choice)
            playNewGame(ai_choice, h_choice, username)

def playNewGame(ai_choice, h_choice, username):
    """
    This manage if person want to play more than 1 game.
    """

    playagain =''
    while playagain != 'Y' and playagain != 'N':
        try:
            playagain = input('\nDo you want play again? [y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')
    if playagain == 'Y':
        playgame(ai_choice, h_choice, username)
    else:
        print('Bay bay!')
        exit()

def whoStart():
    """
    Returns who will start the game ( first move )
    """
    first =''
    while first != 'Y' and first != 'N':
        try:
            clean()
            first = input('Do you want start to play? [y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')
    if first == 'Y':
        return False
    else:
        return  True

def main():
    
    global username, h_choice, ai_choice, winPos
    
    winPos = ((1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7))
    h_choice = '' # X or O
    ai_choice = '' # X or O

    clean()
    username = input('Hello and welcome to Tic Tac Toe Game! \n\nPlease type your player name: ')
    clean()

    #PLAYER SELECT GAME LETTER CHOICE
    while h_choice != 'O' and h_choice != 'X':
        clean()
        try:
            print('')
            h_choice = input(f'{username}, please choose X or O to play: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()

    # SET AI CHOICE
    if h_choice == 'X':
        ai_choice = 'O'
    else:
        ai_choice = 'X'

    playgame(ai_choice, h_choice, username)

if __name__ == '__main__':
    main()
