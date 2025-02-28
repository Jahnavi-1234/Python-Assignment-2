# Original dictionary
dict = {1: 'one', 2: 'two', 3: 'three'}

# New dictionary
new_dict = {}

# Loop through the original dictionary
for key, value in dict.items():
    new_dict[value] = 1  # Set all values to 1 for the new dictionary

# Manually set 'three' to 3
new_dict['three'] = 3

# Output : {'one': 1, 'two': 1, 'three': 3}
print(new_dict)
