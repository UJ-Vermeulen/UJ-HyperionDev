str_manip = input("Enter any sentence! ")

#sentence length
print("\nSentence length")
print(len(str_manip))

#last word replacement using -1 to determine final one
print("\nThe last word replaced by @ throughout entire sentence!")
replacement_str = str_manip[-1]

print(str_manip.replace(replacement_str , '@'))

#backwards string
print("\nThe last 3 letters in reverse!")
print(str_manip [-3:][::-1])

#Is there any way to refine [-3:][::-1]? I initially tried to both detect the last 3 words and reverse print them in one go but I couldnt get it right, so I settled on first identifying then reversing


#create word from first 3 letters and last 2 letters

print('\nNew word created from 3 words from the start and the final 2 words!')

front_three_words = str_manip[:3]
final_two_words = str_manip [-2:]

print(front_three_words + final_two_words)