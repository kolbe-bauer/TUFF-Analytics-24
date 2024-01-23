from tkinter import Tk

from src.file_manager import pick_game

root = Tk()
root.title("Tuff Stat Taking - John Clyde")
# make full screen
root.state('zoomed')


def main():
    game = pick_game(root)
    # point_roster = pick_point_roster(root)


if __name__ == "__main__":
    main()

root.mainloop()
