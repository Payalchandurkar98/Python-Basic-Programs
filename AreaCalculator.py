#Write a program in Python to create area calculator.

print("************ AREA CALCULATOR *************")
print("""Press 1 to get the area of Square.
Press 2 to get the area of Rectangle.
Press 3 to get the area of Circle.
Press 4 to get the area of Triangle.""")

option = int(input("Select an option between 1 to 4: "))

if option == 1:
    side = float(input("Enter side length: "))
    area = side*side
    print("The area of the Square is ", area)
elif option == 2:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length*width
    print("The area of the Rectangle is ", area)
elif option == 3:
    radius = float(input("Enter the radius of the circle: "))
    area = ((22/7)*(radius**2))
    print("The area of the Circle is ", area)
elif option == 4:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 1/2*base*height
else:
    print("Invalid option. Please select the correct option.")



