"""Declaration of Matrix Data Structure"""
# Declaring a matrix of size 3 X 3, and initializing it with value zero
rows, cols = (3, 3)
arr = [[0]*cols]*rows
print(arr)


# Initializing a 2-D array with values
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


""" Traversal of a Matrix Data Structure"""
arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# Traversing over all the rows
for i in range(0, 3):
    # Traversing over all the columns of each row
    for j in range(0, 4):
        print(arr[i][j], end=" ")
    print("")
    
    
    
""" Searching in a Matrix Data Structure"""
def searchInMatrix(arr, x):
    # m=4,n=5
    for i in range(0, 4):
        for j in range(0, 5):
            if(arr[i][j] == x):
                return 1
    return

x = 8
arr = [[0, 6, 8, 9, 11],
       [20, 22, 28, 29, 31],
       [36, 38, 50, 61, 63],
       [64, 66, 100, 122, 128]]
if(searchInMatrix(arr, x)):
    print("YES")
else:
    print("NO")

