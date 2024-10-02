arr = [3, 5, 1, 9, 6, -3]
# arr = [3,5]
# arr = [5, 3]
largest = arr[0]
second = arr[1]
# largest = 0
# second = None
if largest < second:
    largest, second = second, largest
for i in arr[2:]:
    if largest < i:
        second = largest
        largest = i
print(second)
