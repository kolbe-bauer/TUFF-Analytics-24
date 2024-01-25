import tkinter as tk


def insert_field(parent_frame, point):
    scalex = 10
    scaley = 6
    # Create a canvas for drawing
    canvas = tk.Canvas(parent_frame, width=scalex * 40, height=scaley * 110, bg='forest green')
    canvas.grid(row=0, column=0, sticky='nsew', rowspan=10, columnspan=1)

    # Draw fixed elements on the canvas
    draw_fixed_elements(canvas, scalex, scaley)

    # Bind the left mouse click to adding a point
    canvas.bind("<Button-1>", lambda event, canvas=canvas, scalex=scalex, scaley=scaley: set_point(event, canvas, scalex, scaley, point))

    return canvas, scalex, scaley


# Function to add a point to the dataset
def set_point(event, canvas, scalex, scaley, point):
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
    point.add_point_coordinates((scaled_x, scaled_y))
    point.add_unscaled_point_coordinates((x, y))


# deletes the last point
def delete_last_point(canvas, point, scalex, scaley):
    if point.get_point_coordinates() != []:
        canvas.delete("all")
        draw_fixed_elements(canvas, scalex, scaley)
        point.remove_point_coordinates()
        point.remove_unscaled_point_coordinates()
        for dot in point.get_unscaled_point_coordinates():
            x, y = dot[0], dot[1]
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


def redraw_field(canvas, curr_point):
    coordinates = curr_point.get_unscaled_point_coordinates()
    for dot in coordinates:
        x, y = dot[0], dot[1]
        canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill='red')