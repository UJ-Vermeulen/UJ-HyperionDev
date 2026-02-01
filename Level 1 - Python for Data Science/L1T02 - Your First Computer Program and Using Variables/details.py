'''
psuedo code for 1.2.2

Define user name as user_name
    ask user their name
    
Define user age as user_age
    ask user their age
    
Define street name as user_street_name
    ask user their street name

Define house number as user_house_number
    ask user their house number

print out all of these strings in one sentence
    use the format function
    
'''

print('\nPlease enter the following details:')

user_name = input("\nWhat is your name and surname? ")
user_age = input("what is your age? ")
user_street_name = input("What is your street name? ")
user_house_number = input("What is your street number? ")

print(f"\n{user_name} is {user_age} years old and live at house number {user_house_number} on {user_street_name}")