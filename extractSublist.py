# Define a list of numbers
list = [3, 5, 6, 32, 74, 85, 9, 46, 27, 56]
#start index from the user
start_index = int(input("Enter start index: "))
#end index from the user
end_index = int(input("Enter end index: "))
# Create a sublist from the original list using the specified start and end indices
sublist = list[start_index:end_index]
#start_index to end_index-1
print(sublist)
