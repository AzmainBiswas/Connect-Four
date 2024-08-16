import random

from calculate_wins import CalculateWins
from game_components import GameComponents
from game_constants import *
from user_input import UserInput


class Game:
    """
    main game class
    """

    def __init__(self) -> None:
        self.__columns = GameComponents()
        self.__user_input = UserInput()
        self.__cal_win = CalculateWins()
        self.__who_win = GamePlayers.Empty

    def __player_turn(self) -> None:
        """
        player turn until sucessful drop
        """
        sucessful_drop = False
        self.__columns.print_column()

        if self.__cal_win.is_win:
            return

        if self.__columns.is_full:
            return

        user_column = 0
        while not sucessful_drop:
            user_column = self.__user_input.get_column() - 1
            sucessful_drop = self.__columns.drop_to_column(
                user_column, GamePlayers.Player
            )
            if not sucessful_drop:
                print(f"-> column is full!! you cant choose {user_column}")
                print("  tyr chooseing other column")

        # claculate win
        self.__who_win = self.__cal_win.win(
            self.__columns.columns, user_column, self.__columns.top_row_indeces
        )

    def __computer_turn(self) -> None:
        """
        turn for computer
        """
        if self.__cal_win.is_win:
            return

        if self.__columns.is_full:
            return

        avaiable_columns = self.__columns.avaiable_columns
        bot_column = avaiable_columns[random.randint(0, len(avaiable_columns) - 1)]
        self.__columns.drop_to_column(bot_column, GamePlayers.Bot)

        # claculate win
        self.__who_win = self.__cal_win.win(
            self.__columns.columns, bot_column, self.__columns.top_row_indeces
        )

    def main_game_loop(self):
        
        while not self.__cal_win.is_win and not self.__columns.is_full:
            self.__player_turn()
            self.__computer_turn()

        self.__columns.print_column()

        if self.__columns.is_full:
            print("It is a draw.")
            return

        if self.__cal_win.is_win:
            if self.__who_win == GamePlayers.Player:
                print("You won the game..")
                return
            else:
                print("you loose...")

