#first define the inputs

string_fav = input ("What is your favourite restaurant?: ")
int_fav = int(input("What is your favourite number?"))

print(string_fav)
print(int_fav)


#When trying to run this code, Print(int(string_fav)), the error (ValueError: "invalid literal for int() with base 10") appears
# I believe this is happening as the letters are not real numbers, such as 0 or 1, and thus cannot be turned into an integer.
