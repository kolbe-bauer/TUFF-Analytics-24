# Modifying the provided script to include the new features


import tkinter as tk

SCALE = 5

# Function to write points to a text file
def write_points_to_file():
    with open("logged_points.txt", "a") as file:  # Append mode
        #append a point that was just clicked
        file.write(f"X: {points[-1][0]}, Y: {points[-1][1]}")
        file.write("\n")  # New line for each canvas clear

def next_possession_to_file():
    with open("logged_points.txt", "a") as file:  # Append mode
        #append a new line between possessions
        file.write("\n")  # New line for each canvas clear

# Function to add a point to the dataset
def add_point(event):
    x, y = event.x, event.y
    points.append((x//SCALE, 90-y//SCALE))
    canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill='red')  # Draw a red point
    update_point_list()
    write_points_to_file()

# Function to update the point list on the side
def update_point_list():
    point_list.delete(0, tk.END)  # Clear the existing list
    for point in points:
        point_list.insert(tk.END, f"X: {point[0]}, Y: {point[1]}")

# Function to clear the canvas and dataset
def clear_canvas():
    canvas.delete('all')  # Clear the canvas
    draw_fixed_elements()  # Redraw fixed elements
    points.clear()  # Clear the dataset
    update_point_list()
    next_possession_to_file()  # Log clearing in file

# Function to draw fixed elements on the canvas
def draw_fixed_elements():
    # Draw horizontal lines
    canvas.create_line(0, SCALE*20, SCALE*40, SCALE*20)
    canvas.create_line(0, SCALE*90, SCALE*40, SCALE*90)
    canvas.create_line(0, SCALE * .3, SCALE * 40, SCALE * .3)
    canvas.create_line(0, SCALE * 110, SCALE * 40, SCALE * 110)
    canvas.create_line(SCALE * .3, 0, SCALE * .3, SCALE * 110)
    canvas.create_line(SCALE * 40, 0, SCALE * 40, SCALE * 110)
    # Draw fixed dots
    fixed_dots = [(20, 20), (20, 35), (20, 50)]
    for dot in fixed_dots:
        x, y = dot
        canvas.create_oval(SCALE*x - 3, SCALE*(90-y) - 3, SCALE*x + 3, SCALE*(90-y) + 3, fill='blue')

# Create the main application window
root = tk.Tk()
root.title("Coordinate System")

# Create a canvas for drawing
canvas = tk.Canvas(root, width=SCALE*40, height=SCALE*110)
canvas.pack()

# Draw fixed elements on the canvas
draw_fixed_elements()

# Set the coordinate system range
# canvas.create_line(0, SCALE*110, SCALE*40, SCALE*110)  # X-axis
# canvas.create_line(SCALE*20, 0, SCALE*20, SCALE*90)  # Y-axis

# Create a listbox to display points
point_list = tk.Listbox(root)
point_list.pack()

# Create a button to clear the canvas
clear_button = tk.Button(root, text="Clear", command=clear_canvas)
clear_button.pack()

# Initialize the dataset
points = []

# Bind the left mouse click to adding a point
canvas.bind("<Button-1>", add_point)

root.mainloop()

