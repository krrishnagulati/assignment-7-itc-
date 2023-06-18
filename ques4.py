def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged

# Get the number of students from the user
n = int(input("Enter the number of students: "))

# Get the marks for each student
marks = []
for i in range(n):
    mark = int(input(f"Enter the mark for student {i+1}: "))
    marks.append(mark)

# Sort the marks using merge sort
sorted_marks = merge_sort(marks)

# Print the sorted list
print("List after sorting is:", sorted_marks)
