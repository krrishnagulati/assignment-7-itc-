def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Get the input array from the user
input_array = list(map(int, input("Enter the integer array (comma-separated): ").split(',')))

# Sort the array
sorted_array = sorted(input_array)

# Get the element to search from the user
element = int(input("Enter the element to search: "))

# Perform binary search
index = binary_search(sorted_array, element)

if index == -1:
    print("Element not found.")
else:
    count = 1
    # Count the number of occurrences of the element
    # towards the left of the found index
    left = index - 1
    while left >= 0 and sorted_array[left] == element:
        count += 1
        left -= 1

    # Count the number of occurrences of the element
    # towards the right of the found index
    right = index + 1
    while right < len(sorted_array) and sorted_array[right] == element:
        count += 1
        right += 1

    print("Sorted array:", sorted_array)
    print(f"Number of occurrences of element {element} is: {count}")
