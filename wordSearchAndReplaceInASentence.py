# Get a sentence input from the user
Sentence = input("Enter a sentence: ")
# Get the word that the user wants to find in the sentence
word_to_find = input("Enter the word to find: ")
# Get the word that the user wants to use as a replacement
word_to_replace = input("Enter the word to replace: ")
# Replace occurrences of the word_to_find with word_to_replace in the sentence
Modified_sentence = Sentence.replace(word_to_find, word_to_replace)
print(Modified_sentence)
