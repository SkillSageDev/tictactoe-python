class Board:
    range: int = 9
    value: int = 1
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def creat_board(self) -> None:
        self.board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def print_board(self):
        for i in range(len(self.board)):
            if i != 2 and i != 5 and i != 8:
                print(f"{self.board[i]}|", end="")
            else:
                print(self.board[i], end="")
            if i == 2 or i == 5:
                print("\n─╬─╬─")
        print("\n")

    def is_valid_move(self, choice: int) -> bool:
        return self.board[choice - 1].isdigit()

    def update_board(self, choice: int, symbol: str) -> bool:
        if self.is_valid_move(choice):
            self.board[choice - 1] = symbol
            return True
        return False
