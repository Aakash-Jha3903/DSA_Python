# implementation of Selection Sort
arr = [64, 25, 12, 22, 11]

# Traverse through all array elements
for i in range(len(arr)-1):    
    min_idx = i
    for j in range(i+1, len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j
            
    # Swap the found minimum element with the "first" element        
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print("This is your Sorted array : ",arr)