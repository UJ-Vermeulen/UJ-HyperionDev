#“The!quick!brown!fox!jumps!over!the!lazy!dog.”

replace_sentence = 'The!quick!brown!fox!jumps!over!the!lazy!dog.'.replace('!',' ')

print('\nReplaced sentence')
print(replace_sentence)



upper_sentence = 'The quick brown fox jumps over the lazy dog.'.upper()

print('\nUpper case sentence')
print(upper_sentence)



# used print(len("The quick brown fox jumps over the lazy dog."))
#       determined length was 44
#           Allowing me to use [44::-1]

#Further experimenting revealed that the query length is not needed, and only using [::-1] works as well, and this will work with any sentence 

reversed_sentence = 'The quick brown fox jumps over the lazy dog.'[::-1]

print("\nReversed sentence")
print(reversed_sentence )

