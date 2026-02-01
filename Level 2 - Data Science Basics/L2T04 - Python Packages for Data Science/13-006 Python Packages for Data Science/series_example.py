import pandas as pd
import numpy as np

# Here we create a simple pandas series that includes a NaN.
# NaN is used to represent missing values or other undefined entries. 
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

# Note that pandas converts the integers into floats. This is because the NaN
# entry is present.