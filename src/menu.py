class Menu:
    def main(self) -> int:
        return int(
            input(
                "Welcom to XO Game!\n1. start game\n2. quit game\nPlease pick a number!\n"
            )
        )

    def end(self) -> int:
        return int(
            input("Game Over!\n1. restart game\n2. quit game\nPlease pick a number!\n")
        )
