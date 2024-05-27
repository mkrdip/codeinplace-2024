# native import
import random
import time
# local import
from graphics import Canvas


# Constants for canvas dimensions
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
# Title of the canvas window
CANVAS_TITLE = "City Night"
# Colors for different elements
BUILDING_COLORS = ['gray', 'darkgray', 'lightgray']
WINDOW_COLOR = 'yellow'
CAR_COLORS = ['red', 'blue', 'green', 'white']


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT, CANVAS_TITLE)
    canvas.config(bg='black')  # Night sky background

    buildings = draw_buildings(canvas)
    cars = create_cars(canvas)

    print("Watch the city at night!")

    while True:
        move_cars(canvas, cars)
        canvas.update()
        time.sleep(0.05)  # Control the animation speed


def draw_buildings(canvas):
    buildings = []
    building_width = 60
    for x in range(0, CANVAS_WIDTH, building_width):
        building_height = random.randint(CANVAS_HEIGHT//2, CANVAS_HEIGHT - 50)
        top_y = CANVAS_HEIGHT - building_height
        building = canvas.create_rectangle(x, top_y, x + building_width, CANVAS_HEIGHT, color=random.choice(BUILDING_COLORS))
        buildings.append(building)
        # Draw windows
        window_width, window_height = 10, 15
        for wx in range(x + 5, x + building_width - window_width, 20):
            for wy in range(top_y + 5, CANVAS_HEIGHT - window_height, 25):
                canvas.create_rectangle(wx, wy, wx + window_width, wy + window_height, color=WINDOW_COLOR)
    return buildings


def create_cars(canvas):
    cars = []
    car_width, car_height = 40, 20
    for _ in range(5):  # Number of cars
        x = random.randint(0, CANVAS_WIDTH)
        car = canvas.create_rectangle(x, CANVAS_HEIGHT - 40, x + car_width, CANVAS_HEIGHT - 20, color=random.choice(CAR_COLORS))
        cars.append((car, random.uniform(1, 3)))  # Car object and speed
    return cars


def move_cars(canvas, cars):
    for car, speed in cars:
        canvas.move(car, speed, 0)  # Move cars horizontally
        coords = canvas.coords(car)
        if coords[2] > CANVAS_WIDTH:  # Check if car has moved out of screen
            canvas.moveto(car, -40, CANVAS_HEIGHT - 40)  # Reset car position


if __name__ == '__main__':
    main()
