# Definitions
alt_intro = 'Hello World'
joined_alt_intro = ''

# Use a for loop and range feature with an implemented len() to determined the
# length and position where index can be applied in upper or lower case letters
for i in range(len(alt_intro)):
    if i % 2 == 0:
        joined_alt_intro += alt_intro[i].upper()

    else:
        joined_alt_intro += alt_intro[i].lower()

print('\n' + joined_alt_intro)

# I tried applying the join and split features, but could not get it to work
# After experimenting I realised the for loop and index + range combo works
# A variable that will serve as the collection of all words = split_words = ''
alt_sentence = 'I am learning to code'

split_alt_sentence = alt_sentence.split()

split_words = ''

# for loop with an index and range to determine length and position of words
# in list created in above definitions. odd numbers are lower, even are upper
for i in range(len(split_alt_sentence)):
    if i % 2 == 0:
        split_words = split_words + ' ' + split_alt_sentence[i].lower()

    else:
        split_words = split_words + ' ' + split_alt_sentence[i].upper()

final_alt_sentence = ''.join(split_words)

# An additoinal strip to get rid of the leading and lagging a start and end
final_alt_sentence = final_alt_sentence.strip()

# Print the final sentence
print('\n' + final_alt_sentence)
