""


#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        # #Your code here

        # def rotateByOne(arr,t):     # aj ...............
        #     if t == 0:
        #         return arr
        #     n = len(arr)
        #     x = arr[0]
        #     for i in range(1,n):
        #         arr[i-1] = arr[i]
        #     arr[n-1] = x
        #     rotateByOne(arr,t-1)
        
        # return rotateByOne(arr,d)



        # n = len(arr)     # ChatGPT ...................
        # d = d % n  # In case d is greater than n
        
        # # Helper function to reverse the sub-array
        # def reverse(start, end):
        #     while start < end:
        #         arr[start], arr[end] = arr[end], arr[start]
        #         start += 1
        #         end -= 1
                
        # # Step 1: Reverse the first d elements
        # reverse(0, d - 1)
        
        # # Step 2: Reverse the remaining n - d elements
        # reverse(d, n - 1)
        
        # # Step 3: Reverse the entire array
        # reverse(0, n - 1)
        
        
        
        
        
        n = len(arr)    #ChatGPT ...........
        d = d % n  # Normalize d in case it's greater than n
        
        # Use slicing to rotate the array
        arr[:] = arr[d:] + arr[:d]
        
        
        
        
        
        # n = len(arr)  #GFG solution ......................
        # d %= n
        # #First reversing d elements from starting index.
        # arr[0:d] = reversed(arr[0:d])

        # #Then reversing the last n-d elements.
        # arr[d:n] = reversed(arr[d:n])

        # #Finally, reversing the whole array.
        # arr[0:n] = reversed(arr[0:n])
        

        return arr
        
        
        
        
        # for i in range(d):  # takes too much time (not accecpted) !!
        #     arr.append(arr.pop(0))
        # return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ob.rotateArr(A, D)

        for i in A:
            print(i, end=" ")

        print()

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends