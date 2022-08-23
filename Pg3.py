# Python program to demonstrate difference between = and copy()
original = {1: 'Amita', 2: 'Adam'}

# copying using copy() function
new = original.copy()

# removing all elements from new list and printing both
new.clear()
print('new: ', new)
print('original: ', original)


original = {10: 'Mechanical', 2: 'Medical',3:'Electronics'}
# copying using =
new = original

# removing all elements from new list and printing both
new.clear()
print('new: ', new)
print('original: ', original)
