# Syntax error; the parentheses were missing
print("Welcome to the error program")

# Compilation error; incorrect/unnecessary indent.
# Syntax error: missing parentheses
print("\n")

# Indentation error; incorrect/unnecessary indent. + Syntax error;  excess '='
# Runtime error: The original '24 years old', removed 'years old' to allow ↓
# string to be casted into an integer in the next line
age_Str = "24"

# Compilation error; incorrect/unnecessary indent
age = int(age_Str)

# Compilation error; incorrect/unnecessary indent.
# Runtime error; 'I'm" + age + "years old.' caused an error as prior to this ↓
# the age string was converted into an integer. Solution was format {}
print(f"I'm {age} years old.")

# Compilation error; incorrect/unnecessary indent.
# Runtime error; caused problems with the next line. ↓
# This has to be an integer ↓as strings and integers cannot be concatenated
years_from_now = 3

# Compilation error; incorrect/unnecessary indent
total_years = age + years_from_now

# Syntax Error; the parentheses were missing.
# Runtime error; the + "answer_years" was a string and incorrectly labelled ↓
# Solution was to use format {}
print(f"The total number of years:{total_years}")

# Syntax error; incomplete variable name, Correct name was total_years
# Compilation error; statement did not calculate the additional 6 months
total_months = total_years * 12 + 6

# Syntax error; the parentheses were missing;
# Runtime error; strings and integers cannot be concatenated: Solution: format
print(f"In 3 years and 6 months, I'll be {total_months} months old")
