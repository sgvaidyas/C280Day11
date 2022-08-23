l = [11, 2, 333, 1, 44, 5, 66, 777]


b = False

print(l)

swap = True
while swap:
    swap = False
    for each in range(0, len(l)-2, 2):
        k = each+1
        if l[k] > l[k+2]:
            l[k], l[k+2] = l[k+2], l[k]
            swap = True
    if swap: print(l)
swap = True
while swap:
    swap = False
    for each in range(0, len(l)-2, 2):
        k = each
        if l[k] > l[k+2]:
            l[k], l[k+2] = l[k+2], l[k]
            swap = True
    if swap: print(l)
print(l)
