'''
A program that contains a logical error
    math related problem, oversigt in division?
        calculate average with incorrect formula
            divide total input by total number

'''

# Definitions and inputs
total_number = 0
total_input = 0
user_number = float(input('Use -1 to calculate your average! ' +
                          '\nPlease enter a number! '))


# usng a while loop, allowing multple inputs ↓
# and caclulating the number of inputs
while user_number != -1:
    total_number = total_number + user_number
    total_input = total_input + 1
    user_number = float(input('Please enter a number! '))


# else clause, allowing average to be calculated when conditions are met
else:
    total_average = total_input/total_number  # Logic error
    print(f'\nYour total average is {total_average}')
