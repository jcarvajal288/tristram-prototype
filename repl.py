import code

import dungeon
import town


class Repl(code.InteractiveConsole):
    def __init__(self):
        super().__init__()
        self.town = town.Town()
        self.dungeon = dungeon.Dungeon()
        self.town.add_hero()
        self.current_phase = 'dungeon'

    def runsource(self, source, filename="<input>", symbol="single"):
        if source == "" or source == "next":
            self.run_current_phase()
        elif source == "exit" or source == "quit":
            quit()
        else:
            print(f"Unrecognized command: {source}")

    def run_current_phase(self):
        if self.current_phase == 'dungeon':
            self.dungeon.enter(self.town.heroes[0])
            self.current_phase = 'town'
        elif self.current_phase == 'town':
            self.town.visit(self.town.heroes[0])
            self.current_phase = 'dungeon'




def main():
    repl = Repl()
    repl.interact(banner='', exitmsg='')


if __name__ == '__main__':
    main()
