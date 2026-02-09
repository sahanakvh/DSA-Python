# Find the minimum element in an array
arr = [4, 2, 7, 1, 9]
min_element = arr[0]
for num in arr:
    if num < min_element:
        min_element = num
print("Minimum element:", min_element)
