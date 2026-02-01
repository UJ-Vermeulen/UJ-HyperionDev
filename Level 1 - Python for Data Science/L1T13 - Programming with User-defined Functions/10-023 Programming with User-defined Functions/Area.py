"""
This program demonstrates basic functions for calculating the
area of geometric shapes: square, rectangle, and circle.

It also includes a menu-driven program to interactively
calculate these areas based on user input.
"""


def square(length):
    """
    Calculate the area of a square.

    Parameters:
    length (float): The length of one side of the square.

    Returns:
    float: The area of the square.
    """

    return length * length


def rectangle(width, height):
    """
    Calculate the area of a rectangle.

    Parameters:
    width (float): The width of the rectangle.
    height (float): The height of the rectangle.

    Returns:
    float: The area of the rectangle.
    """

    return width * height


def circle(radius):
    """
    Calculate the area of a circle.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The area of the circle.
    """

    return 3.14 * radius ** 2


def options():
    """
    Print the available options for calculating the area of different shapes.
    """

    print("Options:")
    print("s = calculate the area of a square.")
    print("c = calculate the area of a circle.")
    print("r = calculate the area of a rectangle.")
    print("q = quit")


print("This program will calculate the area of a square, circle or rectangle.")
choice = "x"

# Loop until the user chooses to quit ('q')
while choice != "q":
    # Display the available options
    options()

    # Prompt user for their choice
    choice = input("Please enter your choice: ")

    # Check the user's choice and perform corresponding actions
    if choice == "s":
        # Calculate and display area of a square
        length = float(input("Length of square: "))
        print("The area of this square is", square(length))

    elif choice == "c":
        # Calculate and display area of a circle
        radius = float(input("Radius of the circle: "))
        print("The area of the circle is", circle(radius))

    elif choice == "r":
        # Calculate and display area of a rectangle
        width = float(input("Width of the rectangle: "))
        height = float(input("Height of the rectangle: "))
        print("The area of the rectangle is", rectangle(width, height))

    elif choice == "q":
        # Quit the program
        print("")

    else:
        # Handle unrecognized input
        print("Unrecognized option.")
