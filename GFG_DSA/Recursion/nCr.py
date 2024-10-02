def nCr_Naive(n,r):
    def fact(num):
        f=1
        for i in range(1,num+1):
            f = f * i
        return f

    return fact(n)//((fact(n-r))*fact(r))
    
    
def nCr_memo(n, r, memo={}):
# Check if the result is already computed
    if (n, r) in memo:
        return memo[(n, r)]
    
    if r == 0 or r == n:
        return 1
    if r == 1:
        return n
    
    # Store the result in the memo dictionary
    memo[(n, r)] = nCr_memo(n - 1, r - 1, memo) + nCr_memo(n - 1, r, memo)
    return memo[(n, r)]
# return nCr_memo(n,r)


def nCr(n,r):
    if r == 0 or r == n:
        return 1
    if r == 1:
        return n
    
    # Recursive calls ...........
    return nCr(n - 1, r - 1) + nCr(n - 1, r)



#contributed by RavinderSinghPB
# if __name__ == '__main__':
#     tcs=int(input())
    
#     for _ in range(tcs):
#         n,r=[int(x) for x in input().split()]
        
#         print(nCr(n,r))