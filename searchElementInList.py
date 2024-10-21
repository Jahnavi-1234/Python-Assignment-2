list = [3,57,882,487,656,898,253,465]
element_to_find = 882
index = -1
for i in range(len(list)):
    if list[i] == element_to_find:
        index = i
        break
if index != -1:
    print(index)
else:
    print("Element not found in the list.")


