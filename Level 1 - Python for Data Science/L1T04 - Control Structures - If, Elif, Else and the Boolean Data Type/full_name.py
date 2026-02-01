'''
Compulsory Task 1
Follow these steps:

● Create a new Python le in the Dropbox folder for this task, and call it
full_name.py.
This program will be used to validate that a user inputs at least two names when
asked to enter their full name.

● Ask the user to input their full name.

● Perform some validation to check that the user has entered a full name.
Give an appropriate error message if they haven’t. One of the following
messages should be displayed based on the user’s input:
    o “You haven’t entered anything. Please enter your full name.”
    o “You have entered less than 4 characters. Please make sure that you
    have entered your name and surname.”
    o “You have entered more than 25 characters. Please make sure that
    you have only entered your full name.”
    o “Thank you for entering your name.”

The error message examples should help you to determine the sorts of
checks your program will need to perform on the data that the user
provides.
'''

full_name = input("Please enter your full name: ")

if len(full_name) == 0:
        print('You haven’t entered anything. Please enter your full name.')

elif len(full_name) <4:
        print('You have entered less than 4 characters. Please make sure that you have entered your name and surname.')

elif len(full_name) > 25:
        print('You have entered more than 25 characters. Please make sure that you have only entered your full name.')

else :
       print ('Thank you for entering your name.')