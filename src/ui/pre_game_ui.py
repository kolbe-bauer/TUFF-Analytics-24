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

# create center frame which will have most of the things I need to fill out,
# next and back buttons will be separate
def create_center_frame():
    root.update_idletasks()
    # Calculate position to center the frame
    x_pos = (root.winfo_screenwidth()) / 2 - frame_width / 2
    y_pos = (root.winfo_screenheight()) / 2 - frame_height

    center_frame = tk.Frame(root, bg="white", width=frame_width, height=frame_height)
    center_frame.place(x=x_pos, y=y_pos)
    return center_frame


# Function to clear all frames from the root window
def clear_frames(function):
    for widget in root.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()
    # call the function that was passed in
    if function == "start":
        create_start_page()
    elif function == "load":
        load_game()
    elif function == "new":
        new_game()
    else:
        print("ERROR: function not found")

# method to create the start page with the load button and new game button
def create_start_page():
    # create center frame
    center_frame = create_center_frame()
    # create button to load game
    button_load_game = tk.Button(center_frame, text="Load Previous Game", command=lambda: clear_frames("load"),
                                 width=button_width, height=button_height)
    button_load_game.pack(side=tk.TOP)

    # create button to start new game
    button_new_game = tk.Button(center_frame, text="Create New  Game", command=lambda: clear_frames("new"),
                                width=button_width, height=button_height)
    button_new_game.pack(side=tk.BOTTOM)


# method to create the forward and back buttons
def create_forward_back_buttons(previous_page, next_page):
    # create frame for the buttons
    root.update_idletasks()
    # width and height of button
    button_width = 10
    button_height = 2
    # Calculate position to center the frame
    x_pos = (root.winfo_screenwidth()) - frame_width
    y_pos = (root.winfo_screenheight()) - frame_height

    bottom_right_frame = tk.Frame(root, bg="white", width=frame_width, height=frame_height)
    bottom_right_frame.place(x=x_pos, y=y_pos)

    # create back button
    button_back = tk.Button(bottom_right_frame, text="Back\n<=", command=lambda: clear_frames(previous_page),
                            width=button_width, height=button_height)
    button_back.pack(side=tk.LEFT)

    # create forward button
    button_forward = tk.Button(bottom_right_frame, text="Next\n=>", command=lambda: clear_frames(next_page),
                               width=button_width, height=button_height)
    button_forward.pack(side=tk.RIGHT)


# method to create search boxes that will be used multiple times in the pre game ui
def create_searchable_listbox(frame, title, options, row, col):

    frame = tk.LabelFrame(frame, text=title, padx=5, pady=5)
    frame.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

    # Create and place the entry widget
    entry_var = tk.StringVar()
    entry = tk.Entry(frame, textvariable=entry_var)
    entry.pack(fill='x')

    # Create and place the listbox widget
    listbox = tk.Listbox(frame, height=3)
    listbox.pack(fill='both', expand=True)

    # Additional StringVar to store the selected listbox item
    selected_item_var = tk.StringVar()

    def update_listbox(*args):
        search_term = entry_var.get().lower()
        listbox.delete(0, tk.END)  # Clear current listbox entries
        for item in options:
            if search_term in item.lower():
                listbox.insert(tk.END, item)

    def on_enter_pressed(event):
        if listbox.size() > 0:  # Check if the listbox is not empty
            listbox.selection_set(0)  # Select the first item
            selected_option = listbox.get(listbox.curselection())
            selected_item_var.set(selected_option)
            entry_var.set(selected_option)
            update_listbox()
            listbox.delete(0, tk.END)  # Clear the listbox
            entry.icursor(tk.END)  # Move cursor to the end of the entry text
            entry.focus()  # Set focus back to the entry

    def on_select(event):
        if listbox.size() > 0:  # Check if the listbox is not empty
            selected_index = listbox.curselection()
            if selected_index:
                selected_option = listbox.get(selected_index)
                selected_item_var.set(selected_option)
                entry_var.set(selected_option)
                update_listbox()
                listbox.delete(0, tk.END)  # Clear the listbox
                entry.icursor(tk.END)  # Move cursor to the end of the entry text
                entry.focus()  # Set focus back to the entry

    entry_var.trace("w", update_listbox)
    entry.bind("<Return>", on_enter_pressed)
    listbox.bind("<Double-Button-1>", on_select)

    return entry_var, selected_item_var


# method to create the load game page
def load_game():
    # load data from a previous game that was saved
    # create forward and back buttons
    create_forward_back_buttons("start", "point_roster")
    # create center frame
    center_frame = create_center_frame()
    # NEED TO MAKE THIS HAVE THE GAMES THAT HAVE BEEN SAVED
    options = ["option1", "option2", "option3"]
    # make a search box of all the games that have been saved
    entry_var_opponent, selected_opponent_var = create_searchable_listbox(center_frame, "Game", options, 3, 4)


# method to create the new game page
def new_game():
    # create a new game
    # create forward and back buttons
    create_forward_back_buttons("start", "point_roster")
    # create center frame
    center_frame = create_center_frame()
    # NEED TO MAKE THIS HAVE THE TOURNAMENTS AND TEAMS THAT HAVE BEEN SAVED
    options = ["option1", "option2", "option3"]
    # make a search box of all Tournaments
    entry_var_tournament, selected_tournament_var = create_searchable_listbox(center_frame, "Tournament", options, 0, 0)
    # make a search box for the team we are scouting
    entry_var_scouted, selected_scouted_var = create_searchable_listbox(center_frame, "Scouted Team", options, 1, 0)
    # make a search box for the team scouted team is playing
    entry_var_opponent, selected_opponent_var = create_searchable_listbox(center_frame, "Opponent", options, 2, 0)


# call function to create start page
create_start_page()

root.mainloop()
