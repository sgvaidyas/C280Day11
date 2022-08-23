
import random
discounts = ('TEN15', 'TEN20', 'TEN25', 'FIVE10', 'FIVE08', 'FIVE05', 'ONE03', 'ONE04', 'ONE05')

Products = {
    "House": 25000,
    "Country": 60000,
    "Supercar": 6500,
    "Watch": 5500,
    "Bottle": 1200,
    "Pen": 1100
}


def get_discount_code(price):
    L = []
    code = ""
    if (price > 1000 and price < 5000):
        code = "ONE"
    elif (price > 5000 and price < 10000):
        code = "FIVE"
    elif ( price >10000):
        code = "TEN"

    for x in discounts:
        if x.startswith(code):
            code = x.replace(code,"")
            L.append(code)
    return random.choice(L)

while True:
    print("(1): Buy One of Our Products \n(2): Quit")
    option = int(input("Please Choose:"))
    if (option ==1):
        for x in Products:
            x,Products[x]
            print("Product:", x ,"  Price:",Products[x])
        product = input("Please Choose a product to buy: ")
        if(product in Products.keys()):
            price = Products[product]
            print("You have selected :", product ,"@ Price", price )
            print("(1): Generate Discount Code \n(2): DO NOT")
            option = int(input("Please Choose:"))
            if (option ==1):
                discount = int(get_discount_code(price))
                print("Your generated discount code is:", discount)
                print("Bought ", product, "For: ", price*((100-discount)/100))
            else:
                print("Bought " ,product ,"For", price)
        else:
            print("You haven't selected a valid item")
    elif(option == 2):
        print("Quit Successfully...")
        break
    else:
        print("Wrong Option entered")
