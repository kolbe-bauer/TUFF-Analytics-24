import tkinter as tk


button_width = 30
button_height = 5


# Function to clear all frames from the root window
def clear_frames(frame):
    for widget in frame.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()


# create a right frame for the interface
def create_right_frame(parent):
    right_frame = tk.Frame(parent)
    right_frame.pack(side='right', fill='y', expand=True)
    return right_frame


# create a left frame where the canvas will be placed when it is created
def create_left_frame(parent):
    left_frame = tk.Frame(parent)
    left_frame.pack(side='left', fill='y', expand=True)
    return left_frame


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


# create buttons
def create_button(frame, text, command, row, col):
    button = tk.Button(frame, text=text, command=command, width=button_width, height=button_height)
    button.grid(row=row, column=col, sticky='nsew')


# create radio button
# make a bunch of radio buttons for the user to fill out for information
def make_radio_button(parent, options: list, name: str, row, column, rowspan, columnspan):
    frame = tk.LabelFrame(parent, text=name, padx=10, pady=10)
    frame.grid(row=row, column=column, padx=5, pady=5, sticky='nsew', rowspan=rowspan, columnspan=columnspan)

    radio_var = tk.StringVar(value=options[0])
    for i, option in enumerate(options):
        radio_option = tk.Radiobutton(frame, text=option, variable=radio_var, value=option)
        radio_option.pack(anchor='center', expand=True)
    return radio_var


# create drop down menu
def create_option_menu(parent, options, default, command):
    # Create a Tkinter StringVar to hold the current selection
    option_var = tk.StringVar(parent)
    option_var.set(default)

    # Create the OptionMenu and associate it with the parent widget
    option_menu = tk.OptionMenu(parent, option_var, *options, command=lambda selection: command(option_var.get()))
    option_menu.pack()

    return option_menu, option_var
