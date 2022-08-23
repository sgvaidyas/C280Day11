import random
discounts = ('TEN15', 'TEN20', 'TEN25',   'FIVE10', 'FIVE08', 'FIVE05' ,    'ONE03', 'ONE04', 'ONE05' )
products_db = {"Shoes":450_000, 'Banana': 5500, 'Mouse': 1500}
products = list(products_db.keys())
while True:
    for i in products:
        print(i, end="\n")
    number = random.randint(0, 2)
    p , q = input("Please choose a product from the above & select quantity: ").split()
    q = int(q)
    price = products_db[p]
    total_price = price * q
    print("\n")
    print(f"Initial price is {total_price}£")
    if total_price > 10_000:
        code = discounts[number]
        discount = int(code[-2:])
        total_price = total_price - (total_price*discount)/100
        print(f"Discounted price is: {total_price} with a discount of {discount}%")
        # Take tuple index and take int
    elif total_price < 10_000 and total_price > 5_000:
        code = discounts[number+3]
        discount = int(code[-2:])
        total_price = total_price - (total_price*discount)/100
        print(f"Discounted price is: {total_price} with a discount of {discount}%")
    elif total_price < 5_000 and total_price > 1_000:
        code = discounts[number+6]
        discount = int(code[-2:])
        total_price = total_price - (total_price*discount)/100
        print(f"Discounted price is: {total_price}£ with a discount of {discount}%")

