# This example demonstrates how to read data from a file into a pandas DataFrame.
import numpy as np
import pandas as pd

# Read data from the file called 'credit.csv' into a DataFrame
# Remember to specify that the delimiter, in this case it is a single space
article_read = pd.read_csv('credit.csv', delim_whitespace = 1) 

# Prints the entire file that was read in as a DataFrame
print("Entire DataFrame-----------------------------------------------")
print(article_read) 

# Prints a random sample of rows. 
# The number of rows to return is specified as 5. The default is 1. 
print("\nDataFrame sample-----------------------------------------------")
print(article_read.sample(5)) 

# Prints the first 5 rows
print("\nDataFrame head-----------------------------------------------  ")
print(article_read.head())

# Prints the last 3 rows
print("\nDataFrame tail-----------------------------------------------  ")
print(article_read.tail(3))
