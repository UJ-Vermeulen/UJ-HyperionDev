'''Optional Bonus Task 1
Let’s try some slightly more complex maths. Follow these steps:
● Create a new Python le in the Dropbox folder for this task, and call it
optional_task1.py.
● Ask the user to enter the lengths of all three sides of a triangle.
● Calculate the area of the triangle.
● Print out the area.
● Hints
○ If side1, side2 and side3 are the sides of the triangle:
■ s = (side1 + side2 + side3)/2 and
■ area = √(s(s-a)*(s-b)*(s-c))
○ You’ll need to be able to calculate the square root (this may help)
'''

#first import math to access square root function
import math



#define the length of all three sides
print("Please enter the length of all three triangles sides:")
side1 = float(input("\nFirst side's length: "))
side2 = float(input("Second side's length: "))
side3 = float(input("Third side's length: "))



#determine semiperimiter
semi_perimeter = (side1 + side2 + side3)/2



#determine the area
triangle_area = math.sqrt(semi_perimeter*(semi_perimeter-side1)*(semi_perimeter-side2)*(semi_perimeter-side3))

print("\n", triangle_area)