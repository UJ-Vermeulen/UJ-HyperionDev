# Define the inputs, and convert string to float
print("Please enter your triathlon activity times in minutes!")
user_swimming = float(input('What was your swimming time?: '))
user_cycling = float(input('What was your cycling time?: '))
user_running = float(input('What was your running time?: '))

# Determine the sum of all three entered times
triathlon_total_time = (user_swimming + user_cycling + user_running)
print(f"\nYour total time was {triathlon_total_time}!")

# Determine the award based on total time
if triathlon_total_time <= 100:
    print("\nYou have been awarded provincial colours!")

elif triathlon_total_time >= 101 and triathlon_total_time <= 105:
    print("\nYou have been awarded provincial half colours!")

elif triathlon_total_time >= 106 and triathlon_total_time <= 110:
    print("\nYou have been awarded a provincial scroll!")

else:
    print("\nNo award given")
