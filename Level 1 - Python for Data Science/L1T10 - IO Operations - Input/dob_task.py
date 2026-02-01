# The definitions
name_content = ''
dob_content = ''

# Impliment a way to open a file, preferably'with' and 'as'
#   Start a 'for' loop to read every line
#      split every loop
#          use splicing to seperate last 3 and first 2 words, allowing a
#          seperation between date of birth and name
#               join the split list into a string again
with open('DOB.txt', 'r') as file:
    for line in file:
        split_line = line.split()
        dob_content = dob_content + '\n' + ' '.join(split_line[-3:])
        name_content = name_content + '\n' + ' '.join(split_line[:-3])

# Print final variables
print('Name:')
print(name_content)

print('\nDate Of Birth:')
print(dob_content)
