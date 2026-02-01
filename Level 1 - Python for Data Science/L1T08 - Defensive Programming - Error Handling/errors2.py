# Syntax error, the variable was never fully defined ↓
# which later on caused a name error
animal = "Lion"

animal_type = "cub"

number_of_teeth = 16

# Syntax error; variables were entered but never assigned the format function.
# Logic error;  number_of_teeth and animal_type has to be switched around
# Line too long
full_spec = (f"This is a {animal}. It is a {animal_type}" +
             f" and it has {number_of_teeth} teeth")

# Syntax Error; the parentheses were missing
print(full_spec)
