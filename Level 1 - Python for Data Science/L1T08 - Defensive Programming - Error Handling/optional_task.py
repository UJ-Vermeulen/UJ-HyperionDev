print('Give us any two values (x and y) and we will determine their addition' +
      ', multiplication, division, and subtraction')

# definitions and inputs
input_x = input('\nGive us your X value: ') 
  input_y = float(input('Give us your Y value: ')) #Compilation error; this indent will affect the structure and how it is read and must be consistent with other blocks


# Calculations
# Addition
input_addition = input_x + input_y #Runtime error; since input_x was never converted to a float value, it cannot be concatenated as it is a string still
print f'\nThe addition of X,{input_x}, and Y,{input_y}, is {input_addition}!') #Compilation error; a missing parenthesis would prevent pyton from fully executing the print command

# multiplication
input_multipli = input_x * input_y
print(f'\nThe multiplication of X,{input_x},' +
      f' and Y,{input_y}, is {input_multipli}!')

# division
input_division = input_x/input_y
print(f'\nThe division of X,{input_y}, by Y,{input_x}, is {input_division}!') #Logic error; input y and X are switched around, though a calculation will be made, it will be erroneous as it will divide y/x instead of x/y as stated by the string

# subtraction
input_subtraction = input_x - input_y
print(f'\nThe subtraction of Y,{input_y}' +
      f' from X,{input_x}, is {input_subtraction}!')
