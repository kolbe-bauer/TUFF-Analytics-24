from src.ui.shared_ui import clear_frames, create_right_frame, create_button, create_searchable_listbox, make_radio_button, create_option_menu
import tkinter as tk


def point_roster_page(parent_frame):
    clear_frames(parent_frame)
    # create frame for the buttons
    right_frame = create_right_frame(parent_frame)

    # Entry widget for input
    entry_var = tk.StringVar()
    entry = tk.Entry(right_frame, textvariable=entry_var)
    entry.pack()

    # Button to add entries
    add_button = tk.Button(right_frame, text="Add Entry", command=lambda: add_entry(entry_var, listbox))
    add_button.pack()

    # Listbox to display entries
    listbox = tk.Listbox(right_frame)
    listbox.pack()

    # Button to remove selected entry
    remove_button = tk.Button(right_frame, text="Remove Selected", command=lambda: remove_selected(listbox))
    remove_button.pack()


def add_entry(entry_var, listbox):
    # Get the current entry and add it to the Listbox
    entry = entry_var.get()
    if entry:
        listbox.insert(tk.END, entry)
    entry_var.set('')  # Clear the entry widget


def remove_selected(listbox):
    # Remove the selected entry from the Listbox
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)
    except IndexError:
        pass  # No item selected
