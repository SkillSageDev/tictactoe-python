from board import Board
from menu import Menu
from player import Player


class Game:
    menu: Menu = Menu()
    board: Board = Board()
    p1: Player = Player()
    p2: Player = Player()
    players: list = [p1, p2]
    current_player: int = 0

    def start_game(self) -> None:
        choice: int = self.menu.main()
        while True:
            if choice == 1:
                self.board.creat_board()
                self.setup_players()
                self.play_game()
                choice = 0
            elif choice == 2:
                self.quite_game()
                break
            else:
                choice = self.menu.main()

    def play_game(self) -> None:
        while True:
            self.play_turn()
            if self.win_check() or self.draw_check():
                self.board.print_board()
                choice: int = self.menu.end()
                while choice == 1 or choice == 2:
                    if choice == 1:
                        self.restart_game()
                        choice = 2
                    elif choice == 2:
                        break
                    else:
                        choice = self.menu.end()

                break

    def restart_game(self) -> None:
        self.board.creat_board()
        self.play_game()

    def win_check(self) -> bool:
        win_conditions: list = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]

        for a, b, c in win_conditions:
            if self.board.board[a] == self.board.board[b] == self.board.board[c]:
                return True
        return False

    def draw_check(self) -> bool:
        for char in self.board.board:
            if not self.win_check() and char.isdigit():
                return False
        return True

    def setup_players(self) -> None:
        self.players[0].choose_symbol()
        if self.players[0].symbol == "x":
            self.players[1].symbol = "o"
        else:
            self.players[1].symbol = "x"
            print(
                f"Player 1, symbol is: {self.p1.symbol}\nPlayer 2, symbol is: {self.p2.symbol}"
            )

    def play_turn(self) -> None:
        self.board.print_board()
        while True:
            if not self.win_check() or not self.draw_check():
                self.replace_symbol()
                self.switch_player()
                break

    def switch_player(self) -> None:
        self.current_player = 1 - self.current_player

    def replace_symbol(self) -> None:
        print(f"Player {self.current_player + 1}, select a number\n")
        while True:
            try:
                choice: int = int(input())
                if self.board.update_board(
                    choice, self.players[self.current_player].symbol
                ):
                    break
                else:
                    print(
                        f"Invalid Move, the number {choice} is already taken\nPlayer {self.current_player + 1} please choose another number!"
                    )
                    self.board.update_board(
                        choice, self.players[self.current_player].symbol
                    )
            except:
                print("Invalid choice, please enter a number between (1-9)")

    def quite_game(self):
        print("Thanks for playing!")


game = Game()
game.start_game()
