from src.ui.shared_ui import create_left_frame, create_point_roster_selector, clear_frames, create_right_frame, create_button, create_searchable_listbox, make_vert_radio_button, create_option_menu
import tkinter as tk
from Enums.wind import WindDirection
import src.ui.Point as Point



def point_roster_page(parent_frame, time):
    curr_point = Point.Point([], [])
    clear_frames(parent_frame)
    # create frame for the buttons
    right_frame = create_right_frame(parent_frame)

    # create selector for point roster
    create_point_roster_selector(right_frame, "C:\\Users\\jtscl\\PycharmProjects\\TUFF-Analytics-24\\Rosters\\tuff.csv", curr_point)
    # select wind direction for point as well as starting line
    wind_direction_options = [wind_direction.name for wind_direction in WindDirection]
    wind_direction_var = make_vert_radio_button(right_frame, wind_direction_options, "Wind Direction", 2, 1, 2, 1)

    # select Starting Line
    # REPLACE WITH THE ACTUAL ENUM
    starting_line_options = ["O-Line", "D-Line"]
    starting_line_var = make_vert_radio_button(right_frame, starting_line_options, "Starting Line", 0, 1, 2, 1)

    # if its the first time we are on this page for this game, we shouldn't have a back button
    # if its not the first time, we should have a back button that goes to the previous page
    submit_button = create_button(right_frame, "Next", lambda: choose_point_and_thrower(parent_frame), 5, 1, 1, 1)
    if time > 1:
        create_button(right_frame, "Back", lambda: right_frame.destroy(), 6, 1, 1, 1)


def choose_point_and_thrower(parent_frame):
    clear_frames(parent_frame)
    left_frame = create_left_frame(parent_frame)
    right_frame = create_right_frame(parent_frame)

    # put field on the left frame
    insert_field(left_frame)

    # create delete last point button
    create_button(left_frame, "Delete Last Point", lambda: print("delete last point"), 0, 1, 1, 1)

    # create selector for thrower
    thrower = create_option_menu(left_frame, ["thrower1", "thrower2", "thrower3"], "Thrower", lambda selection: print(selection), 2, 1, 1, 1)


def insert_field(parent_frame):
    scalex = 10
    scaley = 6
    # Create a canvas for drawing
    canvas = tk.Canvas(parent_frame, width=scalex * 40, height=scaley * 110, bg='forest green')
    canvas.grid(row=0, column=0, sticky='nsew', rowspan=10, columnspan=1)

    # Draw fixed elements on the canvas
    draw_fixed_elements(canvas, scalex, scaley)

    # Bind the left mouse click to adding a point
    canvas.bind("<Button-1>", lambda event, canvas=canvas, scalex=scalex, scaley=scaley: set_point(event, canvas, scalex, scaley))

# Function to add a point to the dataset
def set_point(event, canvas, scalex, scaley):
    x, y = event.x, event.y
    scaled_x = round(x/scalex, 1)
    scaled_y = round(90-y/scaley, 1)
    if scaled_x < 0:
        scaled_x = 0.0
    elif scaled_x > 40:
        scaled_x = 40.0
    if scaled_y < -20:
        scaled_y = -20.0
    elif scaled_y > 90:
        scaled_y = 90.0

    canvas.create_oval(event.x - 3, event.y - 3, event.x + 3, event.y + 3, fill='red')
    get_coordinates().append((scaled_x, scaled_y))


# deletes the last point
def replot_last_point(canvas):
    canvas.delete("all")
    draw_fixed_elements()
    for x, y in un_scaled_coordinates:
        canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill='red')


def draw_fixed_elements(canvas, scalex, scaley):
    # Draw the Field
    canvas.create_line(0, scaley*20, scalex*40, scaley*20)
    canvas.create_line(0, scaley*90, scalex*40, scaley*90)
    canvas.create_line(0, scaley * .3, scalex * 40, scaley * .3)
    canvas.create_line(0, scaley * 110, scalex * 40, scaley * 110)
    canvas.create_line(scalex * .15, 0, scalex * .15, scaley * 110)
    canvas.create_line(scalex * 40, 0, scalex * 40, scaley * 110)
    # Draw Brick/Midfield marks
    fixed_dots = [(20, 20), (20, 35), (20, 50)]
    for dot in fixed_dots:
        x, y = dot
        canvas.create_oval(scalex*x - 3, scaley*(90-y) - 3, scalex*x + 3, scaley*(90-y) + 3, fill='black')

