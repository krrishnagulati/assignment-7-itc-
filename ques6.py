def remove_duplicates(nums):
    return list(set(nums))

def selection_sort(nums):
    for i in range(len(nums)):
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

def bubble_sort(nums):
    n = len(nums)
    for i in range(n-1):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

# Get the input array from the user
input_array = list(map(int, input("Enter the integer array (comma-separated): ").split(',')))

# Remove duplicates from the array
distinct_array = remove_duplicates(input_array)

# Sort the array using selection sort
selection_sort(distinct_array)
selection_sorted_array = distinct_array.copy()

# Sort the array using bubble sort
bubble_sort(distinct_array)
bubble_sorted_array = distinct_array.copy()

print("Sorted array (Selection Sort):", selection_sorted_array)
print("Sorted array (Bubble Sort):", bubble_sorted_array)
