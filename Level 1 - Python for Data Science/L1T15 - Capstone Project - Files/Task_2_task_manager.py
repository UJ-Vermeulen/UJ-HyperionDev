# =====importing libraries===========

# After researching how to validate dates, datetime was discovered and imported
# To validate date inputs according to the example in tasks, '10 Oct 2019',
from datetime import datetime

# ====Functions====
# ~~~Validation~~~


# Normal string validations, to ensure the user doesn't leave the input blank
# If it complies with it, the input will be returned normally without an
# Error message
def input_validation(prompt_input, error_message):
    while True:
        user_input = input(prompt_input)

        if not user_input:
            print(error_message)

        else:
            return user_input


# Using datetime import, a function can be created for all date inputs and
# Ensure it is in the requested format, if not, the user will be re-prompted
def date_validation(date_input):
    while True:
        user_input = input(date_input)

        try:
            datetime.strptime(user_input, '%d %b %Y')
            return user_input

        except ValueError:
            print(f'\n{user_input} is not in the Day-Month-Year format.' +
                  ' Ex: 1 Oct 2001')


# A function that validates a valid user is used for adding/creating a task
# Read through user list, split password from username.
# If user == assigned user then return input
def user_validation(user_name, error_message):
    with open('user.txt', 'r') as file:
        existing_user = file.readlines()

        while True:
            user_input = input(user_name)

            for line in existing_user:
                ex_username, ex_password = line.strip().split(',')

                if user_input == ex_username:
                    return user_input
            print(error_message)


# Create a simple task status validation for Yes and No, if user uses Y or N
# Then their input will proceed and added to growing string for task
# If user adds nothing or invalid input, then re-prompt and error message
def status_validation(status_check):

    while True:
        task_status = input(status_check).lower()
        if task_status == 'y':
            task_status = 'Yes'
            return task_status

        elif task_status == 'n':
            task_status = 'No'
            return task_status

        else:
            print('Invalid input. Please enter "Y" for Yes or "N" for No.')

# ~~~Menu-functions~~~


# Create a global variable to determine which user is currently logged in
# Will allow it to be used later on in 'view my tasks'
current_user = None


# Open user.txt as file, and use variable to enable each line to be read
# Break the line containing login info into existing username and password
# Use a While loop to pass over ever line to check if entered details are valid
# And is == to that of the existing password and username
# If details match, then return as true, allowing user to access the menu
def user_login():
    global current_user
    with open('user.txt', 'r') as file:
        existing_user = file.readlines()

    while True:
        user_name = input('\nPlease input your username: ')
        user_password = input('Please input your password: ')

        for line in existing_user:
            ex_username, ex_user_password = line.strip().split(', ')

            if user_name == ex_username and user_password == ex_user_password:
                print(f'\nWelcome back, {user_name}!')
                current_user = user_name
                return True

        print('\nYou have entered invalid credentials, please try again!')


# Open user.txt with 'a' to append new data and not overwrite it
# Ask for the new user's name, with an error message for if it is left blank
# Ask user to enter password once, and then again. If both passwords match
# And are not == '', then write it onto the user.txt file
# If passwords do not match, ask user again
def add_user():
    with open('user.txt', 'a') as file:
        while True:
            new_username = input("\nWhat is the new user's name?: ")

            while new_username != '':
                new_password = input("What is the new user's password: ")
                confirm_password = input("Please confirm the password: ")

                if new_password == confirm_password and new_password != '':
                    file.write(f'\n{new_username}, {new_password}')
                    print('User added successfully!')
                    return

                elif new_password == '':
                    print('\nPlease enter a valid password')

                else:
                    print('\nPasswords do not match! Try again.')

            else:
                print('Please enter a valid username!')


# Use a while true loop to ensure everything is completed properly
# Use user validation when asking who the user is for, ensure the user exists
# Validate the inputs of title and description to ensure it isn't blank
# Validate both current and due date, ensure it is in the required format
# Validate the task status input, ensure it is either Y or N
# Once all requirements met, open tasks.txt with A+, to add new data
# And write it to file in the requested order
def add_task():
    while True:
        print('\nTo add a new task, please' +
              ' complete the following information: ')

        task_assigned_to = user_validation('Whose task is this?: ',
                                           "You've entered an invalid user!" +
                                           ' Please add the user first' +
                                           ' or use an existing username!')

        task_title = input_validation('Please give the title of the task: ',
                                      'This field cannot be empty!')

        task_description = input_validation('Describe the task shortly: ',
                                            'This field cannot be empty!')

        task_due = date_validation('When is this task due? Please enter' +
                                   ' it in this "12 Jun 2024" format: ')

        current_date = date_validation("What is the current date? Please" +
                                       " enter it in '12 Jun 2024' format: ")

        task_status = status_validation('Has the task been completed? Y/N: ')

        with open('tasks.txt', 'a+') as file:
            file.write(f'\n{task_assigned_to}, {task_title}' +
                       f', {task_description}, {task_due}, {current_date}, ' +
                       f'{task_status}')
            print('Task added successfully!')
            return True


# Open tasks.txt as read only
# For every line in file, separate the list using split() to split at every ','
# Also strip all unnecessary spaces using strip()
# Once the list is completely broken down into appropriate variables, print it
# In the requested format
def all_tasks():
    with open('tasks.txt', 'r') as file:
        for line in file:
            (task_assignment, task_title, task_description, due_date,
             date_assigned, task_progress) = line.strip().split(', ')

            print(f'''
Task:                 {task_title}
Assigned to:          {task_assignment}
Date assigned:        {date_assigned}
Due date              {due_date}
Task complete?        {task_progress}
Task description:
{task_description}

''')


# Use the global variable  assigned earlier to determine the active user
# Assign a variable as false, to ensure at least one task is printed
# Separate the list into appropriate variables, using split and strip
# If active user == task assigned user then task found = True
# Print the tasks that was assigned to the logged in user
def view_my_tasks():
    global current_user
    with open('tasks.txt', 'r') as file:
        scanned_task = file.readlines()

    tasks_found = False

    for line in scanned_task:
        (task_assignment, task_title, task_description, due_date,
         date_assigned, task_progress) = line.strip().split(', ')

        if current_user == task_assignment:
            if not tasks_found:
                print(f'\nHello, {current_user}! Below are your tasks:')
                tasks_found = True

            print(f'''\n
Task:                 {task_title}
Assigned to:          {task_assignment}
Date assigned:        {date_assigned}
Due date:             {due_date}
Task complete?        {task_progress}
Task description:
{task_description}
''')

    # If no tasks were found
    if not tasks_found:
        print(f"\nYou have no tasks assigned, {current_user}.")


# To determine total amount of users, open user.txt and readlines, then
# Determine the length of the amount of lines
# To determine the total amount of tasks, open tasks.txt to determine the
# Amount of lines(tasks) there are
def display_statistics():
    with open('user.txt', 'r') as file:
        existing_users = file.readlines()
        total_user = len(existing_users)

    with open('tasks.txt', 'r') as file:
        existing_task = file.readlines()
        total_tasks = len(existing_task)

    print(f'''
The statistics are as follows:

Total amount of users: {total_user}
Total amount of tasks: {total_tasks}
''')


# For easier user friendliness, allow user to add another task/ user
# A simple Y(yes)/N(no) input, in a while true loop and error message to ensure
# A valid input
# If user input Y, call the appropriate function to let them add more task/user
def add_more_menu(x, y):
    while True:
        user_input = input(f'''\nWould you like to add another {x}?'
        Y/N: ''').lower()

        if user_input == 'y':
            y()

        elif user_input == 'n':
            print('\nReturning to menu')
            break

        else:
            print('Please enter a valid input!')


# Create a menu for non admin users, with appropriate functions
def normal_menu():
    while True:
        menu = input('''\nSelect one of the following options:
    a - add task
    va - view all tasks
    vm - view my tasks
    e - exit
    : ''').lower()

        if menu == 'a':
            add_task()
            add_more_menu('task', add_task)

        elif menu == 'va':
            all_tasks()

        elif menu == 'vm':
            view_my_tasks()

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have entered an invalid input. Please try again")


# Create an admin menu, with the ability to add users and display statistics
def admin_menu():
    while True:
        menu = input('''\nSelect one of the following options:
    r - register a user
    a - add task
    va - view all tasks
    vm - view my tasks
    ds - display statistics
    e - exit
    : ''').lower()

        if menu == 'r':
            add_user()
            add_more_menu('user', add_user)

        elif menu == 'a':
            add_task()
            add_more_menu('task', add_task)

        elif menu == 'va':
            all_tasks()

        elif menu == 'vm':
            view_my_tasks()

        elif menu == 'ds':
            display_statistics()

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have entered an invalid input. Please try again")


# ====Login Section====
# Call the login function
user_login()

# Once the login has been passed, use a while true Loop for the menu
# Cal appropriate function depending on active user
while True:
    if current_user == 'admin':
        admin_menu()

    else:
        normal_menu()
