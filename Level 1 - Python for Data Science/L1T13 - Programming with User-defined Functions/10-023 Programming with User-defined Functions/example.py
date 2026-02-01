"""
This module provides examples and explanations on defining, calling,
and using functions in Python.
"""


# ========= How to Define a Function ===========
# Defining a function simply means creating a function.
# You begin with the keyword def followed by the name of the function
# and parentheses, ().
# You place any input parameters (values passed to the function)
# within these parentheses.
# You then place a colon ':' after the parentheses to signify the
# start of the indented code block.
# The indented code block contains statements that provide the
# functionality to your function.
# The 'return' can be added, and is used to exit the function
# while also passing a value back to the line that called the function.

# The general syntax of a function in Python is as follows:
# def function_name(parameters):
#     statements
#     return (expression)  # It is possible to create function without a return.


# ************ Example 1 ************

def add_one(x):
    y = x + 1
    return y


# Explanation:
# This function is called 'add_one', it takes as input the parameter 'x'.
# We can call the input variable (here x) anything we want.
# It's just a name we give it so we know how to refer to it
# within the function. Every indented line under the 'def add_one(x):' line
# is 'within' the function.

# The code indented under 'def add_one(x):' is the logic of the function.
# It defines what happens when the function is called.
# Simply put, the function computes a new variable 'y',
# which is the value stored in variable x with 1 added to it.
# It then 'returns' the value y.



# ========= Calling a Function ===========
# In order to execute a function, you need to 'call' it.
# You call a function by using the functions name followed by the values you
# need to pass into the function  within parentheses.


# ************ Example 2 ************
# If you 'called' the function we previously defined with the value of x = 10,
# it would look exactly like this:

print("Example 2: ")
num = 10
print("10 plus 1 is equal to: " + str(add_one(num)) + ".")

# Explanation:
# This will call the function 'add_one' defined above,
# and pass the integer 10 to it.
# The function will then return 11 and it will be printed out.


# ************ Example 3 ************
# You can also call a function and store the value the function returned
# within a variable.

print("\nExample 3: ")
num_plus_one = add_one(4)
print("4 plus 1 is equal to: " + str(num) + ".")

# Explanation:
# Think of the 'call to the function', i.e. 'add_one(4)' , as a 'placeholder'
# for some computation. The function will go off and run its code, and
# in this case, return its result in that place.



# ========= Function Parameters ===========
# In the function definition, you put the names of variables
# that you want to store the input values to, between the parentheses
# after the function name.
# You can put more than one of these variables or parameters,
# simply separate them by commas.


# ************ Example 4 ************
print("\nExample 4: ")


def power(base, exponent):
    # Calculating base raised to the power of exponent.
    result = base ** exponent
    return result


print(power(3, 5))

# Explanation:
# Here we have defined a function named 'power' that takes two parameters:
# 'base' and 'exponent'.
# It calculates the value of 'base' raised to the power of 'exponent'
# using the ** operator, where x ** y means x raised to the power of y.
# In the function call 'print(power(3, 5))', the value 3 is passed to 'base'
# and the value 5 is passed to 'exponent'.


# ************ Example 5 ************
def double_this_number(number):
    y = number * 2  # Multiplies the number by 2.
    return y


# ************ Example 6 ************
def return_first_letter_word(word):
    y = word[0]  # Retrieves the first letter of the input word.
    return y


# ************ Example 7 ************
def put_number_in_list(num):
    new_list = []
    new_list.append(num)  # Adds the input number to a new list.
    return new_list


# ************ Example 8 ************
def put_number_in_list_if_big(num):
    new_list = []
    if num > 100:
        new_list.append(num)  # Only adds the number if it's greater than 100.
    return new_list  # This could return an empty list.


# ************ Example 9 ************
def compute_sum_of_two_numbers(num1, num2):
    y = num1 + num2  # Computes the sum of num1 and num2.
    return y


# ************ Example 10 ************
def takes_no_parameters():
    y = (
        "This function takes no parameters as input, but "
        "that means its functionality is limited...."
    )
    return y


# As you can see from the examples above, you can pretty much do anything
# you want in a function. You can create new data structures,
# use conditionals etc.

# We can call the input variable anything we want.
# It's just a name we give it so we know how to refer to
# it within the function.

# As seen in the 'compute_sum_of_two_numbers' function,
# it is possible to have multiple input parameters.
# There's no limit to how many parameters can be used,
# as long as you can keep track of what's what!

# In 'Example 10', we have a function that takes no input parameters.
# This is also possible, but it means the user who calls the function
# has limited interaction with the function, as they can't supply any input!

# In the case of some functions, imagine a function that returned
# the current time. For example get_time(), in this case it makes sense
# why such a function would not need input parameters.
# However, it may require input parameters if you had a more complex function
# like get_time(timezone). This function might return the time
# for a specific timezone the user provides.
# Values passed into the function through the 'function's parameters',
# e.g. 'num1' and 'num2' above will be referenced with those variable names.
# Think of it as copying in the values from the input parameter values when
# 'calling' the function to these 'function parameters'.


# While the above functions may not seem useful, this is because
# they are simple.
# You can have functions with hundreds of lines that do complex tasks.
# However it is often very useful to define functions
# that do one specific task, with a few lines of codes as opposed to
# a complicated function that does many tasks with hundreds of lines of code,
# i.e. break up a complicated function into many simpler functions so that
# it is easier to understand the function's role and find errors!



# =========== Functions Without Return Statements ===========
# Functions do not need to have a return statement


# ************ Example 11 ************
print("\nExample 11:")


def print_word(word):
    print(word)


# Explanation:
# The function above just prints out something, 
# it doesn't have a return statement.
# That's okay, but it means that if you make a call like:

y = print_word("abc")

# Explanation continued:
# 'y' will store the special value 'None'.
# This is not a string or any other data type,
# so it will cause an error when trying to do other things with it.
# Be careful that your functions return values,
# if that's what you need them to do.


# ************ Example 12 ************
print("\nExample 12:")
# We can call a function multiple times in a loop:

num = 10

for i in range(10):
    num = add_one(num)  
print(num)

# Explanation:
# This loop runs 10 times, and each time, 1 is added to the value of 10.
# So after the first iteration it will be 11, the second iteration computes
# On each iteration the value of num will increase,
# 11 + 1 = 12, etc... until 20, as the loop will run 10 times.



# =========== Scope ===========
# Scope is what we call a program’s ability to find and use variables
# in a program.
# The rule of thumb is that a function is covered in one-way glass:
# it can see out, but no one can see in.
# This means that a function can call variables that are outside the function,
# but the rest of the code cannot call variables
# that are defined within the function.


# *********** Example 13 ****************
print("\nExample 13:")


def do_something():
    print(number)  # Output -> 5


number = 5

do_something()

print(number)  # Output -> 5

# Explanation:
# The above function can see outside and so, it can fetch 'number'
# from outside the function.
# Let's see what happens when this goes wrong.


# *********** Example 14 ****************
print("\nExample 14:")


def do_something():
    number = 7  # 7 is output if 'number' is printed within the function.
    # print(number)  # This would output '7'.


number = 5

print(number)  # Prints 5

do_something()

print(number)  # The output here is still 5.

# Explanation:
# This is because, within the do_something() function,
# 'number' = 7 made a *new* local variable 'number',
# it didn't change the value of the outer 'number' variable.
# To get the function to print out 7, we'd need to place a print statement
# *inside* the function.



# ======================= Play around with Python a bit =====================
#
#   Create a new Python file in this folder called func_practice.py.
#   Inside it, create a function called 'add_three', that takes as input three
#   different parameters num1, num2, num3.
#   Next, write logic to create a new variable, called y,
#   that is the sum of all three of these numbers.
#   Then, return the result y.
#   Now, after you've defined this function, write a function call to return
#   the sum of the numbers 52, 25, and 1403.
#   Store this result in a variable called sum_func.
#   Print out sum_func. Don't forget to cast to a string!
#
# ===========================================================================

# ****************** END OF EXAMPLE CODE ********************* #
