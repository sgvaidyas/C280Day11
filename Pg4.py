d = {'11': 'Diana', '12': 'Sarah'}
print(d.get('11'))

d = {10: 'ten', 20: 'twenty', 30: 'Thirty'}
# since 42 is not in keys, it'll print "Not found"
print(d.get(42, "Not found"))

print(d.get(42,[88,99,66]))
