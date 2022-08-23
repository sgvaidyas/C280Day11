#Python Dictionary setdefault() returns the value of a
# key (if the key is in dictionary).
# Else, it inserts a key with the default value to the dictionary.
d = {'a': 97, 'b': 98, 'c': 99, 'd': 100}
# space key added using setdefault() method
d.setdefault(' ', 32)
print(d)

d = {'a': 97, 'b': 98}
print("setdefault() returned:", d.setdefault('b', 99))
print("After using setdefault():", d)


Dictionary1 = { 'A': 'Apple', 'B': 'Ball'}
print("Dictionary before using setdefault():", Dictionary1)

# using setdefault() when key is non-existing
ret_value = Dictionary1.setdefault('C', "Apple")
print("Return value of setdefault():", ret_value)

print("Dictionary after using setdefault():", Dictionary1)
