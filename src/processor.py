from file_manager import pick_game
import tkinter as tk

root = tk.Tk()
root.title("Pre Game UI")
# make full screen
root.state('zoomed')

def main():
    game = pick_game(root)



root.mainloop()
