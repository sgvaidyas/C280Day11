# initializing dictionary
test_dict = {"Bessy": 7, "Radi": 1, "Andrew": [2,99]}
# Printing initial dict
print("The dictionary before deletion : " + str(test_dict))
# using pop to return and remove key-value pair.
pop_ele = test_dict.pop('Andrew')
# Printing the value associated to popped key
print("Value associated to popped key is : " + str(pop_ele))
# Printing dictionary after deletion
print("Dictionary after deletion is : " + str(test_dict))
