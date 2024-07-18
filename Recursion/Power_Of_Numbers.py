# Recursive code
def power(x, n):
    # x^0 --> return 1
    if (n == 0):
        return 1

    # for 0^y
    if (x == 0):
        return 0

    # For all other cases
    return x * power(x, n - 1)


if __name__ == "__main__":
    x = 2  # x^n
    n = 4

    print(power(x, n))

# Simple Non-Recursive Code
#def Non_Recur():
#    def power(x, n):
#        pow = 1
#        for i in range(n):
#            pow = pow * x
#     return pow
#   x = 2
#   n = 3
#   print(power(x, n))
