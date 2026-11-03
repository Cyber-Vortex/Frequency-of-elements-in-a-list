# Program to find the frequency of elements in a list
data_list = [5, 10, 5, 20, 10, 5, 30, 20]
frequency = {}

# Loop through the list to build the frequency map
for item in data_list:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print("Element Frequencies:")
for element, count in frequency.items():
    print(f"Element {element} appears {count} time(s)")
