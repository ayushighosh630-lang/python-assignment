
import Shapes.shapes as shapes

print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = int(input("Enter choice: "))

if choice == 1:
    r = float(input("Enter radius: "))
    print("Area:", shapes.Area_circle(r))

elif choice == 2:
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    print("Area:", shapes.Area_rectangle(l, b))

elif choice == 3:
    base = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print("Area:", shapes.Area_triangle(base, h))