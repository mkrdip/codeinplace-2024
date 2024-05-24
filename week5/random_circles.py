# Pseudocode for the Program

# 1. Import necessary modules: Canvas from graphics, and random
# 2. Define constants for canvas width, height, maximum circle size, and maximum number of circles
# 3. Define the main function:
#     a. Create a canvas with a specified width and height
#     b. Generate a random number of circles to draw, between 1 and N_CIRCLES
#     c. Loop the random number of times:
#         i. Call the draw_random_circle function with the canvas as an argument
# 4. Define the draw_random_circle function:
#     a. Generate random x and y coordinates within the canvas bounds, ensuring the circle fits within the canvas
#     b. Generate a random circle size
#     c. Calculate the bottom-right coordinates for the circle based on the size
#     d. Call the random_color function to get a random color
#     e. Draw a circle (oval) on the canvas at the calculated coordinates with the random color
# 5. Define the random_color function:
#     a. Define a list of color strings
#     b. Return a random color from the list
# 6. Call the main function if the script is executed directly

# Native import
import random

# Local import
from graphics import Canvas

# Constants for canvas dimensions and circle properties
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
N_CIRCLES = 20

def main():
    """
    Main function to set up the canvas and draw random circles.
    """
    # Create the canvas
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Extension 1: Draw a random number of circles between 1 and 20
    rand_circles = random.randint(1, N_CIRCLES)
    for i in range(rand_circles):
        draw_random_circle(canvas)

def draw_random_circle(canvas):
    """
    Draws a random circle on the given canvas.
    
    Parameters:
        canvas (Canvas): The canvas on which to draw the circle.
    """
    # Extension 3: Ensure all parts of the circle are within the canvas
    x1 = random.randint(0, CANVAS_WIDTH - CIRCLE_SIZE)
    y1 = random.randint(0, CANVAS_HEIGHT - CIRCLE_SIZE)
    
    # Extension 2: Draw circles of a random size
    rand_circle_size = random.randint(5, CIRCLE_SIZE)  # Ensure a minimum size for visibility
    x2 = x1 + rand_circle_size
    y2 = y1 + rand_circle_size
    
    # Get a random color
    color = random_color()
    
    # Draw the circle (oval) on the canvas
    canvas.create_oval(x1, y1, x2, y2, color=color)

def random_color():
    """
    Returns a random color from a predefined list of colors.
    
    Returns:
        str: A string representing a color.
    """
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)

if __name__ == '__main__':
    main()
