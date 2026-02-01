# Define the amount of inputs and total sum of numbers
total_number = 0
total_input = 0
number_input = 0

print("Please enter a series of numbers, and to calculate the average of the numbers entered, enter -1.")

while number_input != -1:
    total_number = total_number + number_input
    number_input = float(input("\nPlease input a number: "))
    total_input = total_input + 1

    if number_input == -1:
        total_input = total_input - 1 #I noticed that the -1 was included in the division, as such I implemented a -1 to the total input as it would require it to be detected first, and then subtracting it from the total
        

print(f"\nThe average is {total_number/total_input}!")