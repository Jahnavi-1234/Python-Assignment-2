# Define the sets
A = {'apple', 'banana', 'orange', 'pineapple', 'lemon', 'grapefruit', 'pear'}
B = {'cranberry', 'cherry', 'orange', 'lichy', 'cucumber', 'banana', 'carrot'}
# Print intersection of A and B
intersection = A & B
print("Intersection:", intersection)
# Print difference A from B
difference_A_B = A - B
print("Difference A from B:", difference_A_B)
# Print difference B from A
difference_B_A = B - A
print("Difference B from A:", difference_B_A)
# Print symmetric difference
symmetric_difference = A ^ B
print("Symmetric Difference:", symmetric_difference)
