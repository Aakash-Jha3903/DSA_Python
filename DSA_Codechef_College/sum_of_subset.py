# s = [2,8,1,9,6,7,11,4]
# subset = []
# index = 0
# while True:
#     for i in s[index:]:
#         subset.append(i)
#         if sum(subset) == 12 :
#             break
#         if sum(subset) > 12:
#             subset = []
#             index += 1
#             continue
#         index += 1

# print(subset)





s = [2, 8, 1, 9, 6, 7, 11, 4]
subset = []
index = 0

while index < len(s):
    for i in s[index:]:
        subset.append(i)
        
        if sum(subset) == 12:
            break
        
        if sum(subset) > 12:
            subset = []
            index += 1
            break  # Break out of the inner loop to restart from a new starting point
    
    if sum(subset) == 12:
        break  # Exit the outer loop when the desired subset is found

print(subset)
