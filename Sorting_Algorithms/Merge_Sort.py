# Merges two subarrays of array[].
# First subarray is arr[left..mid]
# Second subarray is arr[mid+1..right]
def merge(array, left, mid, right):
    subArrayOne = mid - left + 1
    subArrayTwo = right - mid

    # Create temp arrays
    leftArray = [0] * subArrayOne
    rightArray = [0] * subArrayTwo

    # Copy data to temp arrays leftArray[] and rightArray[]
    for i in range(subArrayOne):
        leftArray[i] = array[left + i]
    for j in range(subArrayTwo):
        rightArray[j] = array[mid + 1 + j]

    indexOfSubArrayOne = 0  # Initial index of first sub-array
    indexOfSubArrayTwo = 0  # Initial index of second sub-array
    indexOfMergedArray = left  # Initial index of merged array

    # Merge the temp arrays back into array[left..right]
    while indexOfSubArrayOne < subArrayOne and indexOfSubArrayTwo < subArrayTwo:
        if leftArray[indexOfSubArrayOne] <= rightArray[indexOfSubArrayTwo]:
            array[indexOfMergedArray] = leftArray[indexOfSubArrayOne]
            indexOfSubArrayOne += 1
        else:
            array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo]
            indexOfSubArrayTwo += 1
        indexOfMergedArray += 1

    # Copy the remaining elements of left[], if any
    while indexOfSubArrayOne < subArrayOne:
        array[indexOfMergedArray] = leftArray[indexOfSubArrayOne]
        indexOfSubArrayOne += 1
        indexOfMergedArray += 1

    # Copy the remaining elements of right[], if any
    while indexOfSubArrayTwo < subArrayTwo:
        array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo]
        indexOfSubArrayTwo += 1
        indexOfMergedArray += 1


# begin is for left index and end is right index
# of the sub-array of arr to be sorted
def mergeSort(array, begin, end):
    if begin >= end:
        return

    mid = begin + (end - begin) // 2
    mergeSort(array, begin, mid)
    mergeSort(array, mid + 1, end)
    merge(array, begin, mid, end)


arr = [12, 11, 13, 5, 6, 7]
arr_size = len(arr)
print("Input Array is : ", arr)
mergeSort(arr, 0, arr_size - 1)
print("\nSorted array is : ", arr)
