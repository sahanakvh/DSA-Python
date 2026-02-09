# Check if an array is sorted
arr = [1, 2, 3, 4, 5]
is_sorted = True
for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        is_sorted = False
        break
print("Array is sorted:", is_sorted)
