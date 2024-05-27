# native import
import random
import time
# local import
from graphics import Canvas


# Constants for canvas dimensions and star properties
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
CANVAS_TITLE = "Starfield Simulation" # Title of the canvas window
NUM_STARS = 100
STAR_SPEED = 2
STAR_SIZE = 2
COLORS = ['white', 'yellow', 'cyan', 'magenta']


def main():
    # Create the canvas
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT, CANVAS_TITLE)
    canvas.config(bg="#000000")  # Set background to black

    stars = create_stars(canvas)

    print("Watch the starfield simulation!")

    while True:
        animate_stars(canvas, stars)
        time.sleep(0.01)  # Add a small delay to control the loop timing


def create_stars(canvas):
    """
    Creates initial stars and places them randomly on the canvas.
    
    Parameters:
        canvas (Canvas): The canvas on which to draw the stars.
    
    Returns:
        list: A list of star objects with their respective velocities.
    """
    stars = []
    for _ in range(NUM_STARS):
        x = random.randint(0, CANVAS_WIDTH)
        y = random.randint(0, CANVAS_HEIGHT)
        color = random.choice(COLORS)
        star = canvas.create_oval(x, y, x + STAR_SIZE, y + STAR_SIZE, fill=color)
        velocity = random.uniform(1, STAR_SPEED)
        stars.append((star, velocity))
    return stars


def animate_stars(canvas, stars):
    """
    Animates the stars to move towards the viewer.
    
    Parameters:
        canvas (Canvas): The canvas on which to animate the stars.
        stars (list): A list of star objects with their respective velocities.
    """
    for star, velocity in stars:
        canvas.move(star, 0, velocity)
        x1, y1, x2, y2 = canvas.coords(star)
        # If the star moves out of the bottom edge, reset it to the top
        if y1 > CANVAS_HEIGHT:
            new_x = random.randint(0, CANVAS_WIDTH)
            canvas.moveto(star, new_x, 0)
    canvas.update()


if __name__ == '__main__':
    main()
