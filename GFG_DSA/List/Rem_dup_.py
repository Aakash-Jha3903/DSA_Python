# remove the duplicate elements in a sorted array


def rem_dup(l):
    if len(l) <= 0:
        return l
    n = len(l)
    temp = [0] * n
    for i in range(1, n):
        if l[i] == l[i - 1]:
            # l[i-1] = "-"

            # l.remove(i-1)
            # l.append("-")

            # temp[i] = l[i]
            continue
        else:
            temp[i - 1] = l[i - 1]

    # return l.sort()
    temp[-1] = l[-1]
    return temp


def rem_dup_Comp_with_temp(l):
    if len(l) <= 0:
        return l
    n = len(l)
    # temp = [0] * n
    temp = [l[0]]

    pos = 0
    for i in range(1, n - 1):
        # if temp[i-1] == l[i]:
        if temp[pos] == l[i]:
            # continue
            pass
        else:
            # temp[i] = l[i]  # wrong !!
            # temp.append(l[i])
            # temp[pos] = l[i]   #we are trying to ASSIGN the value at index "x" but we have the length of arr "(x-1)" -->   # wrong !!
            # temp.insert(pos,l[i])  # wrong !!

            # both are working below :
            temp.append(l[i])
            # temp.insert(pos+1,l[i])
            pos += 1  # increment only when the temp and l vales are same
    return temp


arr = []
arr = [1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 6, 7, 8]
#                        t  l
# [1,2,3,0,0,0,0,0,0,0,]
print(rem_dup_Comp_with_temp(arr))


# arr = [1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 6, 7, 8]
# temp = [arr[0]]
# print(type(temp))
