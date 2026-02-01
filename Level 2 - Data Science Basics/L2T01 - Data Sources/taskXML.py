# Import the ElementTree to work with xml files
import xml.etree.ElementTree as ET

# Parse the xml file tp create an ElementTree object
# Get the root element of the object
tree = ET.parse('movie.xml')
root = tree.getroot()

# Iterate over all 'movie' elements, then print a list of tags
print('Tags for each movie:')
for movie in root.iter('movie'):
    print([child.tag for child in movie])

# Iterate over all 'description' elements, then print a list of those tags
print('\nMovie descriptions:')
for description in root.iter('description'):
    print(f'\n{description.text}')


# Create a variable for the favourited and non favourited counts
favourite_count = 0
not_favourite_count = 0

# Use a for loop to determine if it is favourite or a non favourite using
# The 'true' value for favourite, else add it to non favourite
# Once determined, print out both values
for movie in root.iter('movie'):
    if movie.attrib.get('favorite').strip().lower() == 'true':
        favourite_count += 1

    else:
        not_favourite_count += 1

print(f'\nThe amount of favourite movies: {favourite_count}')
print(f'The amount of non-favourited movies: {not_favourite_count}')
