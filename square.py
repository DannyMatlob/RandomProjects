import tkinter as tk
import random
import math

# Create the main window
window = tk.Tk()
window.title("Rainbow Squares")

# Create the canvas
canvas = tk.Canvas(window, width=800, height=600, bg='white')
canvas.pack()

# Define a function to draw a rainbow square on the canvas
def draw_square(x, y, color, size):
    # Draw a square at the given position, with a size of 20x20 pixels and no outline
    canvas.create_rectangle(x, y, x+size, y+size, fill=color, outline='')

def merge_squares(square1, square2):
    #Store Information about the squares being deleted
    x1, y1, x2, y2 = canvas.coords(square1)
    other_x1, other_y1, other_x2, other_y2 = canvas.coords(square2)
    color = canvas.itemcget(square1, 'fill')

    # Delete the squares that need to be deleted
    canvas.delete(square1)
    canvas.delete(square2)
    
    # Draw a new square that is the combination of the two deleted squares
    newSize = ((x2 - x1) + (other_x2 - other_x1))
    draw_square(x1, y1, color, newSize)

def update_squares():
    # Get a list of all the squares on the canvas
    squares = canvas.find_all()

    # Create a list to store the squares that need to be deleted
    squares_to_delete = []

    # Update the position of each square
    for square in squares:
        # Get the current position of the square
        if (len(canvas.find_withtag(square)) > 0):
            x1, y1, x2, y2 = canvas.coords(square)
        else:
            continue

        # Calculate the new position of the square, applying gravitational forces from the other squares
        acceleration_x = 0
        acceleration_y = 0
        for other_square in squares:
            if other_square == square:
                continue
            if not canvas.find_withtag(other_square):
                continue
            other_x1, other_y1, other_x2, other_y2 = canvas.coords(other_square)
            distance = math.sqrt((other_x1-x1)**2 + (other_y1-y1)**2)
            #If two squares are within 5 pixels then we should consider them colliding
            if distance <= 20:
                 # The squares are colliding, add them to the list of squares to delete
                merge_squares(square,other_square)
                break
            mass1 = x2-x1
            mass2 = other_x2-other_x1
            force = 10*mass1*mass2 / distance**2
            acceleration_x += (force * (other_x1-x1) / distance)
            if (acceleration_x > 1):
                acceleration_x = 1
            acceleration_y += (force * (other_y1-y1) / distance)
            if (acceleration_y > 1):
                acceleration_y = 1
            x1 += acceleration_x
            y1 += acceleration_y
            x2 += acceleration_x
            y2 += acceleration_y

            # Redraw the square at the new position
            color = canvas.itemcget(square, 'fill')
            canvas.delete(square)
            draw_square(x1, y1, color, (x2-x1))

    # Schedule the update_squares function to be called again in 50 milliseconds
    window.after(2, update_squares)

# Define a function to draw a rainbow square on the canvas when the left mouse button is held down
def draw_on_click(event):
    # Calculate the x and y coordinates of the mouse cursor
    x, y = event.x, event.y
    # Generate a random color from the rainbow
    
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    color = random.choice(colors)

    # Draw a square at the cursor position
    draw_square(x, y, color, 20)



# Bind the left mouse button to the draw_on_click function
canvas.bind('<Button-1>', draw_on_click)

# Start the update loop
update_squares()

# Run the tkinter event loop
window.mainloop()
