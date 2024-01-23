from src.file_manager import pick_game
from src.game_manager import pick_point_roster
import tkinter as tk

root = tk.Tk()
root.title("Pre Game UI")
# make full screen
root.state('zoomed')

def main():
    game = pick_game(root)
    # point_roster = pick_point_roster(root)

if __name__ == "__main__":
    main()

root.mainloop()
