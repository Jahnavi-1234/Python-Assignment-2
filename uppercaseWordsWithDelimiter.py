#input from the user
sentence = input("Enter a sentence: ")
#delimiter input from the user
delimiter = input("Enter a delimiter: ")
# Split the sentence into individual words
words = sentence.split()
# Initialize an empty list to store uppercase words
uppercase_words = []
# Loop through each word in the list of words
for i in words:
    # Convert the current word to uppercase and append it to the list
    uppercase_words.append(i.upper())
# Join the list of uppercase words into a single string using the specified delimiter
result = delimiter.join(uppercase_words)
print(result)
