# Week 4 - Graphics Notes

## Introduction to the Graphics Library

This week, we'll be using the `graphics` library, a part of Stanford's CS106A course. The library provides a simple interface for creating basic graphical applications. For comprehensive details, refer to the official documentation available at: [CS106A Graphics Library](https://cs106a.stanford.edu/graphics).

### Setting Up the Graphics Library

To use the `graphics` library outside of the Code In Place (CIP) platform, such as in IDEs like PyCharm or Visual Studio Code, follow these steps:

1. **Download the Library**: Download the raw files from [CS106A Graphics Library Files](https://cs106a.stanford.edu/Graphics.zip).
2. **Extract the Files**: Unzip the downloaded file. Inside, you will find a file named `graphics.py`.
3. **Local Import**: Place the `graphics.py` file in your project directory to make it locally accessible. To use the Canvas class or any other part of the graphics library in your script, simply add from graphics import Canvas at the top of your Python file. This statement imports the Canvas class directly from the `graphics.py` file, enabling you to leverage its graphical functionalities in your main program. This technique exemplifies local imports, which allow you to incorporate specific functions or classes from external files into your main program. 
4. **Example Code**: Within the unzipped folder, you'll find a file named `example_graphics.py`. This file serves as a practical reference for utilizing the graphics library effectively. By reviewing the example code, you can gain insights into how various functions and features of the library are implemented, which can help you better understand and apply these elements in your own projects.

### Using the Graphics Library
The following code will use three elements from the library to draw a line, oval and retangle. 

```py
from graphics import Canvas


WIDTH = 600
HEIGHT = 600


def main():
    # create the canvas
    canvas = Canvas(WIDTH, HEIGHT)
    #  create a line
    canvas.create_line(WIDTH, 0, 0, HEIGHT, "red")
    # create a rectangle
    canvas.create_rectangle(0, 0, 400, HEIGHT, color="blue")
    # create an oval
    canvas.create_oval(100, 100, 300, 300, color="green")


if __name__ == '__main__':
    main()

```

Follow this code to create flags of Bangladesh (`5:3`) and Japan (`3:2`) with right color and aspect ratio. Here is a sample project: https://codeinplace.stanford.edu/cip4/share/FgkTEfWM5ugsKxUVUsTk I created to show some countries flags using this `graphics` library. 


## Function Parameters and Return Values

In this lesson, we will learn how to define functions that: 
1) take/accept parameters 
2) return values. 

Understanding how to pass parameters to helper functions and use predefined functions, like `random_color()`, to pick a random color is essential for creating dynamic and reusable code.

### Function Parameters
Parameters are variables that are passed to a function when it is called. They allow functions to accept input and use it within their scope.

In our code, the `draw_random_circle` function takes the canvas as a parameter and draws a circle at a random position with a random color.

### Return Values
A return value is the output that a function sends back to the caller. This allows the function to produce a result that can be used elsewhere in the program.

In our code, The `random_color` function returns a random color from a predefined list of colors.

