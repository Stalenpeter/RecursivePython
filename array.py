arr = [4, 6, 8, 2, 1, 5, 0, 9]
arr2 = []

while arr:  # While there are elements in arr
    min_val = arr[0]  # Assume the first element is the smallest
    for i in arr:
        if i < min_val:
            min_val = i  # Update the smallest element
    arr2.append(min_val)  # Add the smallest element to arr2
    arr.remove(min_val)  # Remove the smallest element from arr

print(arr2)  # Output: [0, 1, 2, 4, 5, 6, 8, 9]
