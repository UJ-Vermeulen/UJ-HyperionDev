'''Compulsory Task 3
Follow these steps:
● Create a new Python le in the Dropbox folder for this task, and call it
numbers.py.
● Ask the user to enter three different integers
● Then print out:
○ The sum of all the numbers
○ The first number minus the second number
○ The third number multiplied by the rst number
○ The sum of all three numbers divided by the third number
'''

#define all the numbers and convert them to float, for incase decimals are used
number_one = float(input("Please enter your first number "))    
number_two = float(input("Please enter your second number "))
number_three = float(input("Please enter your third number "))

#Define the sum as it is requested by two parts of task, allowing easier re-usage
sum_of_three_numbers = number_one+number_two+number_three

print("\nThe sum of all three numbers is:")
print(sum_of_three_numbers)

#first number minus second number
print("\nThe sum of the first number minus the second number is:")
print(number_one - number_two)


#third number multiplied by first number
print("\nThe third number multiplied by the first number is:")
print(number_three * number_one)

#The sum of all three numbers divided by the third number
print("\nThe sum of all three numbers divided by the third number is:")
print(sum_of_three_numbers / number_three)