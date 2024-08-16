"""
contains all the constants for the game
"""

from enum import Enum

NUMBER_OF_COLUMNS = 7
"""number of columns in the game"""
NUMBER_OF_ROWS = 6
"""number of rows in the game"""
WIN_COMBO_NUMBER = 4
"""consicutive number for a symbol to win"""

SYMBOLES = ("o", "P", "C")
""" 
game symboles 
0: empty symbole (o)
1: player symbole (P)
2: game symbole (C)
"""

class GamePlayers(Enum):
    Empty = 0
    Player = 1
    Bot = 2


class CoinFlip(Enum):
    """Enum for coin flip"""
    Head = 1
    Tail = 2


def clear_console():
    """
    clear the console screen
    """
    print("\033[2J")  # clear the console
    print("\033[H")  # set the curser position on top
