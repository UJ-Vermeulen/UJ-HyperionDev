"""
This script demonstrates how to parse an XML file using Python's
xml.etree.ElementTree libray.It reads the XML data from 'movie.xml',
retrieves the root element, and prints out the root's tag and attributes.
Additionally, it iterates through each child element of the root, printing
their tags and attributes.
"""

import xml.etree.ElementTree as ET

# Parse the XML file 'movie.xml' and create an ElementTree object
tree = ET.parse('movie.xml')

# Get the root element of the XML tree
root = tree.getroot()

# Print the tag (name) of the root element
print(root.tag)

# Print the attributes of the root element
print(root.attrib)

# Iterate over each child element of the root and print their tag names
# and attributes
for child in root:
    print(child.tag, child.attrib)
