from tkinter import Button, END, Entry, Frame, Listbox, StringVar

from src.ui.shared_ui import clear_frames, create_right_frame


def point_roster_page(parent_frame: Frame):
    clear_frames(parent_frame)
    # create frame for the buttons
    right_frame = create_right_frame(parent_frame)

    # Entry widget for input
    entry_var = StringVar()
    entry = Entry(right_frame, textvariable=entry_var)
    entry.pack()

    # Button to add entries
    add_button = Button(right_frame, text="Add Entry", command=lambda: add_entry(entry_var, listbox))
    add_button.pack()

    # Listbox to display entries
    listbox = Listbox(right_frame)
    listbox.pack()

    # Button to remove selected entry
    remove_button = Button(right_frame, text="Remove Selected", command=lambda: remove_selected(listbox))
    remove_button.pack()


def add_entry(entry_var: StringVar, listbox: Listbox):
    # Get the current entry and add it to the Listbox
    entry = entry_var.get()
    if entry:
        listbox.insert(END, entry)
    entry_var.set('')  # Clear the entry widget


def remove_selected(listbox: Listbox):
    # Remove the selected entry from the Listbox
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)
    except IndexError:
        pass  # No item selected
