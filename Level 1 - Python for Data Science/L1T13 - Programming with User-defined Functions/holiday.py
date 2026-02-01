# Define the holiday cost, which will be the final calculation needed
def holiday_cost(x, y, z):
    return x + y + z


# Create dictionaries for cities and plane ticket prices
city_option_dict = {'New York, USA': 1,
                    'Toronto, Canada': 2,
                    'Budapest, Hungary': 3,
                    'Venice, Italy': 4,
                    'London, UK': 5,
                    'Sydney, Australia': 6}

# Use another dictionary to ty plane ticket's key to a value
city_flight_price_dic = {1: 14950.00,
                         2: 16237.23,
                         3: 18721.09,
                         4: 15679.04,
                         5: 15679.54,
                         6: 8972.34}


# For better readability, separate sections with relevant titles
print('\n~~~ Destination ~~~')

# Print the list of available cities
print('\nThe city options are the following cities:')
for value, key in city_option_dict.items():
    print(f"{value}: {key}")


# Define plane cost function. Use a while true and try loop for validation
# Allow user to choose between the given dictionaries, if number outside range
# Prompt user to try again and enter within the given option range
# Once valid number entered and flight ticket price determined, return value
def plane_cost():
    while True:
        try:
            city_flight_option = int(input('\nPlease select a city' +
                                           ' (select between 1-6): '))

            if city_flight_option in range(1, 7):
                selected_city_price = float(
                    city_flight_price_dic[city_flight_option])

                return selected_city_price

            else:
                print('\nPlease enter a valid number')

        except ValueError:
            print('\nPlease enter a valid number')


# Define the hotel cost, use a while true loop and try loop for validation
# Once a valid  number of nights entered, prompt user to enter price of hotel
# Once hotel price entered, calculate hotel cost() as nights * price of hotel
# If user is not staying in a hotel and enters 0 , return as 0
def hotel_cost():
    # For better readability, separate sections with relevant titles
    print('\n~~~ Hotel ~~~')
    while True:
        try:
            num_nights = int(input('\nPlease enter the total' +
                                   ' nights you will be staying' +
                                   ' in a hotel: '))
            if num_nights > 0:
                while True:
                    try:
                        hotel_cost_per_night = float(input('\nHow much does' +
                                                           ' your hotel cost' +
                                                           ' per night?: '))

                        if hotel_cost_per_night > 0:
                            return hotel_cost_per_night * num_nights

                        else:
                            print('Please enter a valid number!')

                    except ValueError:
                        print('Please enter a valid number')

            if num_nights == 0:
                return 0

            else:
                print('Please enter a valid number!')

        except ValueError:
            print('Please enter a valid number')


# Define the rental cost, use a while true loop and try loop for validation
# Once a valid  number of days entered, prompt user to enter price of car/day
# Once rental price entered, calculate rental cost() as nights * rent/day
# If user is not renting a car and enters 0 for days, return as 0
def rental_cost():
    # For better readability, separate sections with relevant titles
    print('\n~~~ Car rental ~~~')
    while True:
        try:
            total_rent_days = int(input('\nPlease enter the total' +
                                        ' days you will be renting a car: '))

            if total_rent_days > 0:
                while True:
                    try:
                        rental_cost_per_day = float(input('\nHow much' +
                                                          ' does the car' +
                                                          ' cost per day?: '))

                        if rental_cost_per_day > 0:
                            return rental_cost_per_day * total_rent_days

                        else:
                            print('Please enter a valid number!')

                    except ValueError:
                        print('Please enter a valid number')

            if total_rent_days == 0:
                return 0

            else:
                print('Please enter a valid number!')

        except ValueError:
            print('Please enter a valid number')


# Define all functions to show summary of expenses
total_plane_cost = plane_cost()
total_hotel_cost = hotel_cost()
total_car_rent_cost = rental_cost()

print(f'\nYour trip summary is: \n Plane ticket: {total_plane_cost}'
      f'\n Hotel: {total_hotel_cost} \n Rental car: {total_car_rent_cost}')

# Calculate the holiday cost and define it to allow for format in print
complete_holiday_cost = holiday_cost(total_car_rent_cost, total_hotel_cost,
                                     total_plane_cost)

# Finally, print the total price for holiday
print(f'\nThe total price for this holiday is R{complete_holiday_cost}!')
