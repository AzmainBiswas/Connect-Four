from game_constants import *

class UserInput:
    """
    handels user inputs
    """

    def __init__(self) -> None: ...

    def __input_number(self, lower_bound: int, upper_bound: int) -> int:
        """
        get user input between two integer

        Parameters:
        lower_bound (int): lower bound (Included)
        upper_bound (int): upper bound (Excluded)

        Return:
        integer given by the user
        """
        input_number: int = -1

        while True:
            try:
                input_string: str = input("> Choose: ")
                input_number: int = int(input_string)
            except Exception:
                print("-> Invalid input!!! please enter a valid number")
                print("   try again ..")
                continue

            if input_number >= lower_bound and input_number < upper_bound:
                return input_number

            print("-> number is out of range!!! choose a valid number.")
            print("   try again ...")

    def get_column(self) -> int:
        """
        get column number from user

        Return:
        column number
        """
        print(f"> Choose a column(1 to {NUMBER_OF_COLUMNS}) to drop symbole")
        return self.__input_number(1, NUMBER_OF_COLUMNS + 1)

    def get_coin_flip(self) -> CoinFlip:
        """
        get coin flip input from user
        
        Return:
        enum of CoinFlip
        """
        print("> Fliping a coin choose your options")
        print("  1) to Head")
        print("  2) to Tail")
        user_responce = self.__input_number(1,3)
        return CoinFlip(user_responce)
        
