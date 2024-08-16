from game_constants import *


class CalculateWins:
    def __init__(self) -> None:
        self.__is_win = False

    @property
    def is_win(self):
        """
        return if win or not
        """
        return self.__is_win

    def __vertical_win(
        self, columns: list[list[int]], column_number: int, top_indeces: list[int]
    ) -> GamePlayers:
        """
        Calculate the vertical win

        Parameters:
        columns (list[list[int]]): game columns.
        column_number (int): column number where the last symbole droped.
        top_indeces (list[int]): list of top indeces


        Return:
        Who win
        """
        if top_indeces[column_number] < WIN_COMBO_NUMBER - 1:
            return GamePlayers.Empty  # if top index is less then 3 win can't happen

        row = top_indeces[column_number]
        count = 1

        while row > 0:
            if columns[column_number][row] == columns[column_number][row - 1]:
                count += 1
                row -= 1
            else:
                break

        if count == WIN_COMBO_NUMBER:
            self.__is_win = True
            return GamePlayers(columns[column_number][top_indeces[column_number]])
        else:
            return GamePlayers.Empty

    def __horizontal_win(
        self, columns: list[list[int]], column_number: int, top_indeces: list[int]
    ) -> GamePlayers:
        """
        Calculate the horizontal win

        Parameters:
        columns (list[list[int]]): game columns.
        column_number (int): column number where the last symbole droped.
        top_indeces (list[int]): list of top indeces


        Return:
        Who win
        """
        row = top_indeces[column_number]
        left_index = column_number
        left_count = 0
        right_index = column_number
        right_count = 1

        # check <-
        while left_index > 0:
            if columns[left_index][row] == columns[left_index - 1][row]:
                left_count += 1
                left_index -= 1
            else:
                break

        # check ->
        while right_index < NUMBER_OF_COLUMNS - 1:
            if columns[right_index][row] == columns[right_index + 1][row]:
                right_count += 1
                right_index += 1
            else:
                break

        if left_count + right_count >= WIN_COMBO_NUMBER:
            self.__is_win = True
            return GamePlayers(columns[column_number][top_indeces[column_number]])
        else:
            return GamePlayers.Empty

    def win(
        self, columns: list[list[int]], column_number: int, top_indeces: list[int]
    ) -> GamePlayers:
        """
        Calculate win

        Parameters:
        columns (list[list[int]]): game columns.
        column_number (int): column number where the last symbole droped.
        top_indeces (list[int]): list of top indeces


        Return:
        Who win
        """
        who_win: GamePlayers = self.__vertical_win(columns, column_number, top_indeces)

        if not self.__is_win:
            who_win = self.__horizontal_win(columns, column_number, top_indeces)

        return who_win
