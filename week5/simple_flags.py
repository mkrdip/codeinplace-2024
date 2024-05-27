# local import: graphics module from Stanford CS106A
from graphics import Canvas


def draw_japan(canvas, width, height):
    """
    Draws the flag of Japan on the given canvas.
    
    Parameters:
        canvas (Canvas): The canvas on which to draw the flag.
        width (int): The width of the flag.
        height (int): The height of the flag.
    """
    # Draw white background
    canvas.create_rectangle(0, 0, width, height, color="#FFFFFF")  
    # Draw red circle (centered)
    canvas.create_oval(width // 2 - height // 6, height // 2 - height // 6,
                       width // 2 + height // 6, height // 2 + height // 6, color="#BC002D")  


def draw_bangladesh(canvas, width, height):
    """
    Draws the flag of Bangladesh on the given canvas.
    
    Parameters:
        canvas (Canvas): The canvas on which to draw the flag.
        width (int): The width of the flag.
        height (int): The height of the flag.
    """
    # Draw green background
    canvas.create_rectangle(0, 0, width, height, color="#006A4E")  
    # Draw red circle (slightly off-center to the left)
    canvas.create_oval(width // 3 - height // 6, height // 2 - height // 6,
                       width // 3 + height // 6, height // 2 + height // 6, color="#F42A41")  


def draw_poland(canvas, width, height):
    """
    Draws the flag of Poland on the given canvas.
    
    Parameters:
        canvas (Canvas): The canvas on which to draw the flag.
        width (int): The width of the flag.
        height (int): The height of the flag.
    """
    # Draw white top half
    canvas.create_rectangle(0, 0, width, height // 2, color="#FFFFFF")  
    # Draw red bottom half
    canvas.create_rectangle(0, height // 2, width, height, color="#DC143C")  


def draw_monaco(canvas, width, height):
    """
    Draws the flag of Monaco on the given canvas.
    
    Parameters:
        canvas (Canvas): The canvas on which to draw the flag.
        width (int): The width of the flag.
        height (int): The height of the flag.
    """
    # Draw red top half
    canvas.create_rectangle(0, 0, width, height // 2, color="#CE1126")  
    # Draw white bottom half
    canvas.create_rectangle(0, height // 2, width, height, color="#FFFFFF")  


def draw_indonesia(canvas, width, height):
    """
    Draws the flag of Indonesia on the given canvas.
    
    Parameters:
        canvas (Canvas): The canvas on which to draw the flag.
        width (int): The width of the flag.
        height (int): The height of the flag.
    """
    # Draw red top half
    canvas.create_rectangle(0, 0, width, height // 2, color="#FF0000")  
    # Draw white bottom half
    canvas.create_rectangle(0, height // 2, width, height, color="#FFFFFF")  


def draw_palau(canvas, width, height):
    """
    Draws the flag of Palau on the given canvas.
    
    Parameters:
        canvas (Canvas): The canvas on which to draw the flag.
        width (int): The width of the flag.
        height (int): The height of the flag.
    """
    # Draw light blue background
    canvas.create_rectangle(0, 0, width, height, color="#87CEFA")  
    # Draw yellow circle (slightly off-center to the left)
    canvas.create_oval(width // 3 - height // 10, height // 2 - height // 10,
                       width // 3 + height // 10, height // 2 + height // 10, color="#FFD700")  


def main():
    """
    Main function to prompt user for a flag choice and draw the selected flag.
    """
    width = 640
    height = 400
    title = "Simple Flags"
    canvas = Canvas(width, height, title)

    # Print menu options for the user
    print("Choose a flag to draw:")
    print("1. Japan")
    print("2. Bangladesh")
    print("3. Poland")
    print("4. Monaco")
    print("5. Indonesia")
    print("6. Palau")
    
    # Get user choice
    choice = int(input("Enter the number of your choice: "))
    
    # Draw the chosen flag
    if choice == 1:
        draw_japan(canvas, width, height)
    elif choice == 2:
        draw_bangladesh(canvas, width, height)
    elif choice == 3:
        draw_poland(canvas, width, height)
    elif choice == 4:
        draw_monaco(canvas, width, height)
    elif choice == 5:
        draw_indonesia(canvas, width, height)
    elif choice == 6:
        draw_palau(canvas, width, height)
    else:
        print("Invalid choice.")

    canvas.mainloop()


if __name__ == '__main__':
    main()
