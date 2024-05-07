# Notes for Week 1: Hospital Karel

## Approching a Problem

1) Understand
    - Write stuff down.
    - Explain the problem out loud to someone.
    - Draw a picture.
2) Strategize
    - Walk through an example or two.
    - Look for patterns.
    - Think about what things you’ll need: loops, conditions, helper functions, etc.

3) Translate
    - First into pseudocode.
    - Then into Python.

## Control Flow

![image](https://github.com/mkrdip/codeinplace-2024/assets/3819579/da88cb29-1514-4101-9f03-2dc7c6328d5e)



The flowchart in our presentation slide outlines when to use different programming structures based on certain conditions. It starts by asking if we have a backup plan. If we don't, we use an if statement. If we do have a backup plan, we need to determine if the action is a one-time thing or something we'll repeat. For one-time actions, an if/else statement works best. For actions we know we'll repeat a set number of times, we use a for loop. If we're not sure how many times we'll need to repeat the action, we should use a while loop.

## Some Useful Python Syntax to Remember

- We use `#` to start a single-line comment. We can use CTRL + `/` in Windows/Linux or Command + `/` in macOS.

- The following is an example of multi-line comment in Python

```py
"""
Here is the multi-line comment in Python.
We use three quotes for it on both sides. 
"""
```

- In Python, colons `:` and indentation (using either `four spaces`) are crucial for defining the structure of the code.
- The colon is used in Python to indicate the start of an indented block, which follows control structures such as loops, conditional statements, function definitions, and more.
- In this example below:
  ```py
    def turn_right():
      for i in range(3):
          turn_left()
  ```
    - The colon in `def turn_right():` indicates the beginning of the function's body.
    - The colon in `for i in range(3):` indicates the start of the loop block.
    - The Python style guide, PEP 8, recommends using four spaces per level of indentation to ensure code readability and consistency across various code editors and coding environments.

- Except for global variables and constants, every other code needs to be placed inside a function.

## Function Precondition and Postcondition

From our `hospital_karel.py` program, let's take an example of the following code to investigate pre and post conditions in a function, also showing an example of function documentation using multiple line comments.

```py
def do_one_column():
    """
    Karel builds a single column of a hospital.
    Pre-condition: Karel is facing east at the bottom
        of where we want to build a column.
    Post-condition: Karel is facing east at the bottom
        of the column it just built.
    """
    turn_left()         # Turn to face north for vertical column construction
    put_three_beepers() # Place three beepers vertically
    move_to_base()      # Move to the bottom of the column
    turn_left()         # Turn left to face east again, ready for the next steps
```

## Decomposition

The concept of decomposition in programming involves breaking down a complex problem into smaller, manageable parts (functions or modules) that can be developed, maintained, and debugged independently. Each part performs a specific task and can be combined with others to solve the overall problem. The `do_one_column` function above from the Hospital Karel program is a great example of decomposition.

**Benefits of Decomposition:**
- Modularity: The do_one_column function is a self-contained module that can be tested and debugged independently of the rest of the program.
- Reusability: This function can be reused in any situation where Karel needs to build a single column, whether as part of a hospital or another structure.
- Simplicity: Decomposing the problem into smaller parts like the above simplifies the main program logic, making it easier to understand and maintain.

