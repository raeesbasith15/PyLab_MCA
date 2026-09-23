pi = 3.14
def area(radius):
    return pi * radius * radius
def perimeter(radius):
    return 2 * pi * radius

radius = float(input("Enter the radius of the circle: "))
circle_area = area(radius)
circle_perimeter = perimeter(radius)

print(f"Area of the circle: {circle_area:.2f}")
print(f"Perimeter of the circle: {circle_perimeter:.2f}") 