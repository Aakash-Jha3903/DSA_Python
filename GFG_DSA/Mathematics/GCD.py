def GCD(a,b):
    if a%b==0:
        return b
    elif b%a==0:
        return a
    else:
        return GCD(b%a,a)
    return a if b == 0 else GCD(b, a % b)

print(GCD(21,18))