from tkinter import Frame, Tk

from src.file_manager import pick_game

root = Tk()
root.title("Tuff Stat Taking - John Clyde")
# make full screen
root.state('zoomed')


def main():
    frame_canvas = Frame(root)
    game = pick_game(frame_canvas)
    # point_roster = pick_point_roster(root)


if __name__ == "__main__":
    main()

root.mainloop()
