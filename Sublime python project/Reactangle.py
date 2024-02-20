# Function to calculate the area of a rectangle
def rectangle_area(length, width):
    area = length * width
    return area

# Example usage
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area_of_rectangle = rectangle_area(length, width)

print(f"The area of the rectangle is: {area_of_rectangle}")
