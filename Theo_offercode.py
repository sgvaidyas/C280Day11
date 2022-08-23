import random

def printCatalog():
    print("\033[1;36m              Catalog")
    print("1. New tires             |    $299.00")
    print("2. Sports Spoiler        |    $799.00")
    print("3. New Premium Oils      |     $42.00")
    print("4. Chevrolet Spark       | $14,595.00")
    print("5. BMW k6 Motorbike      |  $3,795.00")
    print("6. Blinker Fluid         |  $6,495.00")
    print("--------------------------------------\033[0;0m")


def task3():
    print("\033[1;34m--------------------------------------")
    print("| Welcome to Theo's Motor Dealership |")
    print("--------------------------------------\033[0;0m")
    total = 0
    itemList = []
    discountCodes = ('TEN15', 'TEN20', 'TEN25', 'FIVE10', 'FIVE08', 'FIVE05', 'ONE03', 'ONE04', 'ONE05')
    catDict = {1: ["New tires", 299], 2: ["Sports Spoiler ", 799], 3: ["New Premium Oils", 42],
               4: ["Chevrolet Spark", 14595], 5: ["BMW k6 Motorbike", 3795], 6: ["Blinker Fluid", 6495]}
    while True:
        print("1. View Catalog\n2. Add item to basket\n3. Proceed to checkout\n4. Exit")
        print("------------------------")
        print("\033[0;32mBasket Value: $ " + str(total) + "\033[0;0m")
        print("------------------------")
        n1 = int(input("Select an action: "))
        if n1 == 4:
            break
        elif n1 == 1:
            printCatalog()
        elif n1 == 2:
            n2 = int(input("Which item would you like to add: "))
            total += int(catDict.get(n2)[1])
            print("Added a " + catDict.get(n2)[0] + " to the basket.")
            print("------------------------")
        elif n1 == 3:
            totalAfter = 0
            if total > 10000:
                stringCode = discountCodes[random.randint(0, 2)]
                numCode = ""
                for i in stringCode:
                    if i.isdigit():
                        numCode += i
                totalAfter = total * (1 - int(numCode) / 100)
            elif 10000 > total > 5000:
                stringCode = discountCodes[random.randint(3, 5)]
                numCode = ""
                for i in stringCode:
                    if i.isdigit():
                        numCode += i
                totalAfter = total * (1 - int(numCode) / 100)
            else:
                stringCode = discountCodes[random.randint(6, 8)]
                numCode = ""
                for i in stringCode:
                    if i.isdigit():
                        numCode += i
                totalAfter = total * (1 - int(numCode) / 100)
            if total > 0:
                print("\033[1;36m------------------------")
                print("Total before: $ " + str(total))
                print("Discount Code: " + stringCode)
                print("Total After Discount: $ " + str(round(totalAfter, 2)))
                print("------------------------")
                print("\033[1;34mThank you for buying from us!")
                break
            else:
                print("\033[1;34mNo products were added to the basket.")
                print("Thank you viewing us!")


if __name__ == '__main__':
    task3()
