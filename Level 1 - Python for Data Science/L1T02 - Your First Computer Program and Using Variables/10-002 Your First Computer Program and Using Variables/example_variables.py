# PLEASE ENSURE YOU OPEN THIS FILE IN VS Code otherwise you will not be able to run it.

# *** NOTE ON COMMENTS ***
# This is a comment in Python. 
# Comments can be placed anywhere in Python code and the computer ignores them -- they are intended to be read by humans. 
# Any line with a # in front of it is a comment.
# Please read all the comments in this example file and all others.

# ========= How to Declare Variables ===========
# When you declare a variable, you determine its name and data type
# In Python however you do not need to indicate the data type of the variable.
# This is because Python detects the variable's data type by reading how data is assigned to the variable.
# You use the assignment operator ‘=‘ to assign a value to a variable.

# ************ Example 1 ************
num = 2
# the variable num is assigned the integer or whole number 2, due to the presence of digits and lack of quotation marks

# ************ Example 2 ************
num2 = 12.34
# the variable num2 is assigned the float or decimal number 12.34, due to the presence of the decimal point and lack of quotation marks

# ************ Example 3 ************
greeting = "Hello, World!"
# the variable greeting is assigned the String Hello, World!, due to the presence of quotation marks ("...")

# ************ Example 4 ************
number_str = "10"
# Watch out! Since you defined 10 within quotation marks, Python knows this is a String. It's not an integer even though we understand 10 is a number.

# ========= Changing a Value Held by a Variable  ===========
# If you want to change a value held by a variable, simply assign it another value 

# ************ Example 5 ************
num3 = 4
num3 = 5
# this changes the integer value 4 held in num3 to 5

# ========= Casting ===========
# Casting basically means taking a variable of one particular data type and “turning it into” another data type
# To do this you need to use the following functions:
#   str() - converts variable to String
#   int() - converts variable to Integer
#   float() - converts variable to Float

# ************ Example 7 ************
# Using str() to convert an Integer to String

number = 10                     
number_str2 = str(number)
print("Example 7: ")
print(number_str2)

# ************ Example 8 ************
# Using int() to convert a Float to Integer

number_float = 99.99
number_int = int(number_float)
print("Example 8: ")
print(number_int)

# run this example; notice that number_int does not contain a decimal?

# ****************** END OF EXAMPLE CODE ********************* # 

# ======================= Play around with Python a bit  ===========================================
# 
#         At this point, why not play around with creating variables? Create your own python file inside VS Code and try the following.
#         
#         name = "John"  
# 
#         Then press the 'Run' button. Nothing happens but this Python program has remembered what you set the variable 'name' to.
#         To prove this, add to your program: 
# 
#         print(name)
# 
#         and then hit Run. 'John' should be printed out by the program. 
#         
#         We write Python code statements in IDEs like VS Code so that all our variable definitions and code are saved.
#         We can then run these files as Python programs at any time we want, and we can use these programs repeatedly.
#         You are actually writing Python code already, it's that simple!
# 
# ==================================================================================================

