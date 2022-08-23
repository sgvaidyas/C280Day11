a = [11, 2, 333, 1, 44, 5, 66, 777,8]

for x in range(len(a)):

    print(a)
    print()
    smallest = a[x]
    smallestIx = -1
    for y in range(x + 2, len(a), 2):
        if a[y] < smallest:
            smallestIx = y
            smallest = a[y]
    if smallestIx != -1:
        a[x], a[smallestIx] = a[smallestIx], a[x]

print(a)
