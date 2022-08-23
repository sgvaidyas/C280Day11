import random

messages = {"Aquarius": "A beautiful, smart, and loving person will be coming into your life.",
"Pisces": "A dubious friend may be an enemy in camouflage.",
"Aries": "A faithful friend is a strong defense.",
"Taurus": "A faithful friend is a strong defense.",
"Gemini": "A feather in the hand is better than a bird in the air.",
"Cancer": "A fresh start will put you on your way.",
"Leo": "A friend asks only for your time not your money.",
"Virgo": "A friend is a present you give yourself.",
"Libra": "A gambler not only will lose what he has, but also will lose what he doesn't have.",
"Scorpius": "A golden egg of opportunity falls into your lap this month.",
"Sagittarius": "A good friendship is often more important than a passionate romance.",
"Capricorn": "A hunch is creativity trying to tell you something."}

print()
name = input("What's your name? ")
day = eval(input("Please enter your birth day: "))
month = eval(input("Please enter your birth month: "))


if (month == 1 and day > 19) or (month == 2 and 18 > day):
    sign = "Aquarius"
elif (month == 2 and day > 20) or (month == 3 and 20 > day):
    sign = "Pisces"
elif (month == 3 and day > 21) or (month == 4 and 20 > day):
    sign = "Aries"
elif (month == 4 and day > 19) or (month == 5 and 21 > day):
    sign = "Taurus"
elif (month == 5 and day > 20) or (month == 6 and 22 > day):
    sign = "Gemini"
elif (month == 6 and day > 21) or (month == 7 and 23 > day):
    sign = "Cancer"
elif (month == 7 and day > 22) or (month == 8 and 23 > day):
    sign = "Leo"
elif (month == 8 and day > 22) or (month == 9 and 23 > day):
    sign = "Virgo"
elif (month == 9 and day > 22) or (month == 10 and 24 > day):
    sign = "Libra"
elif (month == 10 and day > 23) or (month == 11 and 22 > day):
    sign = "Scorpius"
elif (month == 11 and day > 21) or (month == 12 and 22 > day):
    sign = "Sagittarius"
elif (month == 12 and day > 21) or (month == 1 and 20 > day):
    sign = "Capricorn"

signs = ["Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpius", "Sagittarius", "Capricorn"]

limit = random.randint(50, 100)
x = 0
while x < limit:
    randomSigns = random.sample(signs, 2)
    tempMessage = messages[randomSigns[0]]
    messages[randomSigns[0]] = messages[randomSigns[1]]
    messages[randomSigns[1]] = tempMessage
    x += 1


print()
print("{}, You are a {}".format(name, sign))
print(messages[sign])
print()
