'''
Make lists and dictionaries
    use for loop for item in menu
        determine item value by * stock and price
            determine total stock w
                print total stock worth
'''
# Definitions
total_stock_worth = 0

# Create the list and dictionaries using 4 items, their stock value and price
menu = ['coffee', 'muffin', 'tea', 'cookie']

stock = {'coffee': 120,
         'muffin': 17,
         'tea': 130,
         'cookie': 21
         }

menu_price = {'coffee': 21.99,
              'muffin': 25.00,
              'tea': 19.99,
              'cookie': 10.00
              }

# use the 'for' loop to find the item in the menu
# utilise += to make code more efficient by adding new item value to ↓
# pevious stock worth
for item in menu:
    item_value = (stock[item] * menu_price[item])
    total_stock_worth += item_value

print(f"Your total stock's total worth is R{total_stock_worth}c")
