class Player:
    symbol: str

    def choose_symbol(self) -> str:
        self.symbol = input("Player 1, choose a symbol! (x/o)\n")
        while True:
            if self.symbol == "x" or self.symbol == "o":
                break
            else:
                self.symbol = input(
                    f'The symbol you have chosen "{
                        self.symbol
                    }" is invalid. Please choose "x" or "o"\n'
                )
        return self.symbol
