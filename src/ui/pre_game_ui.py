import tkinter as tk


root = tk.Tk()
root.title("Record Game Data")
root.state('zoomed')
root.configure(bg='white')

# Central frame dimensions
frame_width = 200
frame_height = 100
button_width = 30
button_height = 5


def create_start_page():
    # Calculate position to center the frame
    x_pos = (root.winfo_screenwidth()) / 2 - frame_width / 2
    y_pos = (root.winfo_screenheight()) / 2 - frame_height

    center_frame = tk.Frame(root, bg="gray", width=frame_width, height=frame_height)
    center_frame.place(x=x_pos, y=y_pos)

    # create button to load game
    button_load_game = tk.Button(center_frame, text="Load Game", command=LoadGame, width=button_width, height=button_height)
    button_load_game.pack(side=tk.TOP)

    # create button to start new game
    button_new_game = tk.Button(center_frame, text="New Game", command=NewGame, width=button_width, height=button_height)
    button_new_game.pack(side=tk.BOTTOM)


def LoadGame():
    pass

def NewGame():
    pass


# call function to create start page
create_start_page()

root.mainloop()
