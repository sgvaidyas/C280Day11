import random

sign = input("Enter Zodiac Sign: ")
sign = sign.lower()

zodiac = {
    "libra": ['friendly', 'extroverted', 'cosy'],
    "scorpio": ['determined', 'brave', 'ambitious'],
    "sagittarius": ['loyal', 'honest', 'secretive'],
    "capricorn": ['enthusiastic', 'organized', 'practical'],
    "aquarius": ['self-reliant', 'advanced', 'exceptional'],
    "pisces": ['emotionally-sensitive', 'gracious', 'considerate'],
    "aries": ['ambitious', 'Honest', 'creative'],
    "taurus": ['hardworking', 'dedicated', 'dependable'],
    "gemini": ['flexible', 'extroverted', 'clever'],
    "cancer": ['emotional', 'temperamental', 'spiteful'],
    "lio": ['Compassionate', 'big-hearted', 'romantic'],
    "virgo": ['humble', 'industrious', 'practical'],
}

farewellMessage = ['Keep it up!!', 'have a good day :)', 'GoodBye!!!', 'See you Next time :))']

if sign in zodiac:
    print("You are a", random.choice(zodiac[sign]) + " Person!!!")
    print(random.choice(farewellMessage))
else:
    print("Please Enter a valid zodiac sign")
