
# Defined terms
pattern_variable = 0
asterix_pattern = ""


for pattern_variable in range(0,10): #I initially used range 1:6, but noticed this affected my 'reverse' pattern and learned that it will count from 1-5 and wont be enough turns to complete the pattern
    if pattern_variable < 5:                                  
        asterix_pattern = asterix_pattern + "*"
        print(asterix_pattern)       

    else:
        reverse_pattern = asterix_pattern[:-1] #I tried using ' - "*" ' but kept getting an input error, so I used the slicing technique. Please let me know if there is a better solution
        print(reverse_pattern)
        asterix_pattern = reverse_pattern # I learned if I do not re-define it it will keep printing 4 stars only

