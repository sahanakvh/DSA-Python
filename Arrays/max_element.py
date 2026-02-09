# Find the maximum element in an array

arr = [3, 1, 5, 2, 9]
max_element = arr[0]

for num in arr:
    if num > max_element:
        max_element = num

print("Maximum element:", max_element)
