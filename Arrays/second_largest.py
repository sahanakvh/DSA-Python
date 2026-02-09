# Find the second largest element in an array
arr = [10, 5, 20, 8]
largest = second_largest = -1
for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print("Second largest element:", second_largest)
