from rich import print

from game_constants import *


# contain all the game components
class GameComponents:
    """
    game components contain game columns
    and function to print columns
    """

    def __init__(self) -> None:
        self.__columns: list[list[int]] = [
            [0 for _ in range(NUMBER_OF_ROWS)] for _ in range(NUMBER_OF_COLUMNS)
        ]
        self.__top_row_indeces: list[int] = [
            -1 for _ in range(NUMBER_OF_COLUMNS)
        ]  # keep track of top row indces

    @property
    def columns(self) -> list[list[int]]:
        """get the columns of the game."""
        return self.__columns

    @property
    def top_row_indeces(self) -> list[int]:
        """get the total array of top row indeces."""
        return self.__top_row_indeces

    @property
    def avaiable_columns(self) -> list[int]:
        """gives the list of avaiable columns"""
        return [i for i in range(NUMBER_OF_COLUMNS) if self.__top_row_indeces[i] != NUMBER_OF_ROWS - 1]

    @property
    def is_full(self) -> bool:
        """return if the columns are full or not"""
        for index in self.__top_row_indeces:
            if index != WIN_COMBO_NUMBER:
                return False
        return True

    def print_column(self) -> None:
        """print the columns of the game"""
        columns_string: str = ""

        for row in range(NUMBER_OF_ROWS - 1, -1, -1):
            for col in range(NUMBER_OF_COLUMNS):
                if self.__columns[col][row] == 0:
                    columns_string += f"  [bold black]{SYMBOLES[self.__columns[col][row]]}[/bold black]"
                elif self.__columns[col][row] == 1:
                    columns_string += f"  [bold green]{SYMBOLES[self.__columns[col][row]]}[/bold green]"
                elif self.__columns[col][row] == 2:
                    columns_string += (
                        f"  [bold red]{SYMBOLES[self.__columns[col][row]]}[/bold red]"
                    )
            columns_string += "\n"

        columns_string += "[bold blue]"
        columns_string += "".join("  _" for _ in range(NUMBER_OF_COLUMNS))
        columns_string += "[/bold blue]\n"
        columns_string += "".join(f"  {i + 1}" for i in range(NUMBER_OF_COLUMNS))

        columns_string += "\n"
        clear_console()
        print(columns_string)

    def find_top_index(self, column_number: int) -> int:
        """
        find the top index of a particuler column.

        Parameters:
        column_number (int) index starts from 0

        Return:
        the top index of a particuler column
        """
        return self.__top_row_indeces[column_number]

    def drop_to_column(self, column_number: int, who_drop: GamePlayers) -> bool:
        """
        drop a symbol to a particuler column.

        Parameters:
        column_number (int): which column to drop the symbol (in 0 index)
                             should be between 0 to NUMBER_OF_COLUMNS
        who_drop (int 1 or 2): who drop the symbol 1 or 2 only

        Return:
        true if drop is sucessful
        """
        if column_number not in range(NUMBER_OF_COLUMNS):
            raise IndexError("Index out of range. column_number is not valid.")

        if self.__top_row_indeces[column_number] == NUMBER_OF_ROWS - 1:
            return False

        self.__top_row_indeces[column_number] += 1
        self.__columns[column_number][self.__top_row_indeces[column_number]] = who_drop.value

        return True


