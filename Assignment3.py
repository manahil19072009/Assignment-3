# Input three numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Calculations
sum_result = a + b + c
difference = a - b - c
product = a * b * c
average = sum_result / 3

# Output
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Average:", average)

# Triangle
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
triangle_area = 0.5 * base * height
print("Area of triangle:", triangle_area)

# Square
side = float(input("Enter side of square: "))
square_area = side * side
print("Area of square:", square_area)

# Circle
radius = float(input("Enter radius of circle: "))
circle_area = 3.142 * radius ** 2
print("Area of circle:", circle_area)

# Rectangle
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
rectangle_area = length * width
print("Area of rectangle:", rectangle_area)

# Input two variables
x = input("Enter value of x: ")
y = input("Enter value of y: ")

# Swapping
x, y = y, x

# Output
print("After swapping, x =", x)
print("After swapping, y =", y)
