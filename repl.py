import code

from combat import enter_dungeon


class Repl(code.InteractiveConsole):
    def runsource(self, source, filename="<input>", symbol="single"):
        if source == "run":
            enter_dungeon()
        elif source == "exit":
            quit()
        else:
            print(f"Unrecognized command: {source}")


if __name__ == '__main__':
    repl = Repl()
    repl.interact(banner='', exitmsg='')
