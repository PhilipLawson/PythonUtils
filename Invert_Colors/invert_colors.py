"""
Create a function that inverts the rgb values.
"""

def color_invert(rgb):
    # Check if all values are between 0-255
    if all(0 <= value <= 255 for value in rgb):
        # Invert the RGB values and store them in a new tuple
        inverted_rgb = tuple(255 - value for value in rgb)
        print(inverted_rgb)
        return inverted_rgb
    else:
        print("Error: Each value must be between 0 and 255.")
        return None


def main():
    try:
        # Take user input and store the ints in a tuple called rgb
        rgb = tuple(int(input(f"Enter the value for {color} (0-255): ")) for color in 'RGB')
        # Run the function to invert the RGB values
        color_invert(rgb)
    except ValueError:
        print("Error: Please enter valid integers between 0 and 255")
        return None


if __name__ == "__main__":
    main()