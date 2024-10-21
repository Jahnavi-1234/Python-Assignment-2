fruits = {'apple', 'banana', 'orange', 'pineapple', 'lemon', 'grapefruit', 'pear'}
#Discard 'apple'
fruits.discard('apple')
print(fruits)
#Remove 'banana'
fruits.remove('banana')
print(fruits)
#Try to discard and remove 'cranberry'
fruits.discard('cranberry')  # Discarding will not raise an error
print(fruits)
# Remove 'cranberry' (this will raise an error if 'cranberry' is not in the set)
if 'cranberry' in fruits:
    fruits.remove('cranberry')  # Only remove if it exists
else:
    print("Cranberry not found for removal.")
#Clear the rest
fruits.clear()
print(fruits)
