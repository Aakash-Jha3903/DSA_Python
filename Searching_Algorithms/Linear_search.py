def search(arr, target):

    for i in enumerate(arr):
        if (arr[i[0]] == target):
            return i[0]
    return -1


if __name__ == "__main__":
    input_arr = [32, 13, 90, 50, 40]
    target_element = 50

    result = search(input_arr, target_element)

    if result == -1:
        print("Element is not present in array")
    else:
        print("Element is present at index", result)
