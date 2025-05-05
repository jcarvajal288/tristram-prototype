import code

import dungeon
import town


class Repl(code.InteractiveConsole):
    def __init__(self):
        super().__init__()
        self.town = town.Town()
        self.town.add_hero()

    def runsource(self, source, filename="<input>", symbol="single"):
        if source == "run":
            self.town.visit(self.town.heroes[0])
            dungeon.enter_dungeon(self.town.dungeon, self.town.heroes[0])
        elif source == "exit" or source == "quit":
            quit()
        else:
            print(f"Unrecognized command: {source}")


def main():
    repl = Repl()
    repl.interact(banner='', exitmsg='')


if __name__ == '__main__':
    main()
