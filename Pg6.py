# Dictionary with two keys
Dictionary1 = {'P': 'Patryk', 'B': 'Beatrice'}
# Printing keys of dictionary
print("Keys before Dictionary Updation:")
keys = Dictionary1.keys()
print(keys)
# adding an element to the dictionary
Dictionary1.update({'P': 'Plamen'})
# adding an element to the dictionary
Dictionary1.update({'T': 'Theo'})
print('\nAfter dictionary is updated:')
print(keys)
print("values  = ",Dictionary1.values())
print(list(Dictionary1.values()))
