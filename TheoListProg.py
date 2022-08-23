def task2():
    listA = [11, 2, 333, 1, 44, 5, 66, 777]
    print("Original list:")
    print(listA)
    print("-------------")
    swapped = 1
    while swapped == 1:
        swapped = 0
        for i in range(0, len(listA) // 2 + 1, 2):
            if listA[i] > listA[i + 2]:
                tmp = listA[i]
                listA[i] = listA[i + 2]
                listA[i + 2] = tmp
                swapped = 1
            if listA[i + 1] > listA[i + 3]:
                tmp = listA[i + 1]
                listA[i + 1] = listA[i + 3]
                listA[i + 3] = tmp
                swapped = 1

            print(listA)
    print("Sorted list:")
    print(listA)


if __name__ == '__main__':
    task2()
