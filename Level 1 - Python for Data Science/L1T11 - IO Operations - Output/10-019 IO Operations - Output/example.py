# =========== Write Method ===========
# You can use the write() method in order to write to a file.
# The syntax for this method is as follows:
#   file.write("string")   - writes "string" to the file

# ************ Example 1 ************
# Before you can write to a file you need to open it.
# You open a file using Python's built-in open() function which creates a file
# called output.txt (it doesn't exist yet) in write mode.
# Python will automatically create this file in the same directory/folder 
# that our program is in.

ofile = open('output.txt', 'w')

# We ask the user for their name. When they enter it, it is stored as a string 
# in the variable 'name'.
name = input("Enter your name: ")

# We use the write method to write the contents of the 'name' variable to the output file.
ofile.write(name + "\n")


# You must run this Python file for the file 'output.txt' to be created with the
# output from this program in it.
ofile.write("My name is on the line above in this text file.")
# When we write to the file again, the current contents of the file will not be 
# overwritten. The new string will be written on the second line of the text file.

ofile.close() # Don't forget to close the file!



# ****************** END OF EXAMPLE CODE ********************* #



