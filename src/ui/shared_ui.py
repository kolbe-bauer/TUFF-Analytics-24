import tkinter as tk
import csv



# Function to clear all frames from the root window
def clear_frames(frame):
    for widget in frame.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()


# create a right frame for the interface
def create_right_frame(parent):
    right_frame = tk.Frame(parent, bg='white')
    right_frame.pack(side='right', fill='y', expand=True)
    return right_frame


# create a left frame where the canvas will be placed when it is created
def create_left_frame(parent):
    left_frame = tk.Frame(parent, bg='white')
    left_frame.pack(side='left', fill='y', expand=True)
    return left_frame


# method to create search boxes that will be used multiple times in the pre game ui
def create_searchable_listbox(frame, title, options, row, col, rowspan, columnspan, show_number):

    frame = tk.LabelFrame(frame, text=title, padx=5, pady=5)
    frame.grid(row=row, column=col, padx=5, pady=5, sticky='nsew', rowspan=rowspan, columnspan=columnspan)

    # Create and place the entry widget
    entry_var = tk.StringVar()
    entry = tk.Entry(frame, textvariable=entry_var)
    entry.pack(fill='x')

    # Create and place the listbox widget
    listbox = tk.Listbox(frame, height=show_number)
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
def create_button(frame, text, command, row, col, rowspan, columnspan):
    button = tk.Button(frame, text=text, command=command, width=30, height=5, bg='chocolate3')
    button.grid(row=row, column=col, sticky='nsew', rowspan=rowspan, columnspan=columnspan)


# create radio button
# make a bunch of radio buttons for the user to fill out for information
def make_vert_radio_button(parent, options: list, name: str, row, column, rowspan, columnspan):
    color = 'chocolate3'
    frame = tk.LabelFrame(parent, text=name, padx=10, pady=10, bg=color)
    frame.grid(row=row, column=column, padx=5, pady=5, sticky='nsew', rowspan=rowspan, columnspan=columnspan)

    radio_var = tk.StringVar(value=options[0])
    for i, option in enumerate(options):
        radio_option = tk.Radiobutton(frame, text=option, variable=radio_var, value=option, bg=color)
        radio_option.pack(anchor='center', expand=True)
    return radio_var


def make_ho_radio_button(parent, options: list, name: str, row, column, rowspan, columnspan):
    color = 'chocolate3'
    frame = tk.LabelFrame(parent, text=name, padx=10, pady=10, bg=color)
    frame.grid(row=row, column=column, padx=5, pady=5, sticky='nsew', rowspan=rowspan, columnspan=columnspan)

    radio_var = tk.StringVar(value=options[0])
    for i, option in enumerate(options):
        radio_option = tk.Radiobutton(frame, text=option, variable=radio_var, value=option, bg=color)
        radio_option.grid(row=0, column=i, sticky='nsew')
    return radio_var


# create drop down menu
def create_option_menu(parent, options, default, command, row, col, rowspan, columnspan):
    color = 'chocolate3'
    # Create a Tkinter StringVar to hold the current selection
    option_var = tk.StringVar(parent)
    option_var.set(default)

    # Create the OptionMenu and associate it with the parent widget
    option_menu = tk.OptionMenu(parent, option_var, *options, command=lambda selection: command(option_var.get()))
    option_menu.grid(row=row, column=col, padx=5, pady=5, sticky='nsew', rowspan=rowspan, columnspan=columnspan)

    return option_menu, option_var


def create_point_roster_selector(parent, teamfile, point):
    # read in the team roster to choose from
    # List to hold the formatted lines
    formatted_lines = []

    # Open the CSV file
    with open(teamfile) as csvfile:
        reader = csv.DictReader(csvfile)

        # Loop over each line in the CSV
        for row in reader:
            # Format the line as "First_Name Last_Name #Number"
            formatted_line = f"{row['First_Name']} {row['Last_Name']} #{row['Number']}"

            # Append the formatted line to the list
            formatted_lines.append(formatted_line)

    # create search box
    person_entry_var, person_selected = create_searchable_listbox(parent, "Team Roster", formatted_lines, 0, 0,
                                                                  1, 1,10)

    # Button to add entries
    add_button = tk.Button(parent, text="Add Entry", command=lambda: add_entry(person_entry_var, listbox, point), bg='chocolate3')
    add_button.grid(row=1, column=0, sticky='ew')

    # Listbox to display entries
    listbox = tk.Listbox(parent)
    listbox.grid(row=2, column=0, sticky='nsew')

    # Button to remove selected entry
    remove_button = tk.Button(parent, text="Remove Selected", command=lambda: remove_selected(listbox, point), bg='chocolate3')
    remove_button.grid(row=3, column=0, sticky='ew')


def add_entry(entry_var, listbox, point):
    # Get the current entry and add it to the Listbox
    entry = entry_var.get()
    if entry and entry not in listbox.get(0, tk.END):
        listbox.insert(tk.END, entry)

    entry_var.set('')  # Clear the entry widget


def remove_selected(listbox, point):
    # Remove the selected entry from the Listbox
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)
    except IndexError:
        pass  # No item selected
