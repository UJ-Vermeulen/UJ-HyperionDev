'''
Ask user how many students: include a Value error validation
    create file
        use amount of students for a variable that will
        serve as an input-countdown
            prompt user to start inputting the IDs : include another
            value error validation
                once countdown reach 0
                    break loop and print list in file

'''

# Definitions
complete_student_list = ''

# The initial while true loop, to ensure the user enters a valid number that↓
# be turned into an integer and serve as a countdown for the list
# After failing how to use the except valueerror function and research, ↓
# the 'try' function was discovered and allowed a proper validation check ↓
# that is simple and reruns the input until a valid number is etered
# Once valid number entered, break while true loop
while True:
    try:
        total_student_count = int(input('Please enter the amount of students' +
                                        ' that will be' +
                                        ' attending this venue : '))
        break

    except ValueError:
        print('Please enter a valid number')

# Start the open/create file with W+
# start the initial loop, stating if total student count is != that more↓
# ID inputs will be prompted
# Include a while true and try function to allow for an ValueError validation↓
# Ensures that user enters a valid number and not a letter or blank
# if a valid number entered, remove 1 from the total student count and repeat
# Add all ID inputs together under a new variable
# Once student count == 0, write final ID variable on file
with open('reg_form.txt', 'w+') as file:
    while total_student_count != 0:
        while True:
            try:
                student_id = int(input('Please input a student ID : '))
                break

            except ValueError:
                print('\nPlease enter a valid student ID')

        total_student_count = total_student_count - 1
        complete_student_list = (str(complete_student_list) +
                                 '\n' + str(student_id) + '\t..........')

        if total_student_count == 0:
            file.write('Student ID' + '\t/Signature' + '\n' +
                       complete_student_list)
