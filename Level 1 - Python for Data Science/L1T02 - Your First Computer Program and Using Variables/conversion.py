'''Compulsory Task 3
Follow these steps:
 ● Create a new Python file in this folder called conversion.py
 ● As in the previous compulsory tasks, please first provide pseudo code as
 comments in your Python file, outlining how you will solve this problem.
 ● Declare the following variables:
    ○ num1=99.23
    ○ num2=23
    ○ num3=150
    ○ string1 = “100”

Convert them as follows:
    ○ num1 into an integer
    ○ num2 into a float
    ○ num3 into a string
    ○ string1 into an integer

Print out all the variables on separate lines
'''

'''
psuedo code for 1.2.3

Define the following given variables
    num1 = 99.23
    num2 = 23
    num3 = 150
    string1 = "100"

once defined, declare each of the variables 
    print(type(defined variable))

once declared, convert
    num1 into integer using print(int(num1))
    num2 into a float using print(float(num2))
    num3 into a string using print(str(num3))
    string1 into a integer using print(int(string1))

'''
#Define

num1 = 99.23
num2 = 23
num3 = 150
string1 = "100"

#Declare

print("\nThe variables' declarations are as follow:")

print('\nnum1 = ', type(num1))
print('num2 = ', type(num2))
print('num3 = ', type(num3))
print('string1 = ', type(string1))

print ("\nThe conversions are as follow: ")

print('\nnum1 = ', int(num1))
print('num2 = ', float(num2))
print('num3 = ', str(num3))
print('string1 = ', int(string1))