# It is used to create mappings

dict = {
    1: "Number",
    "One": "String"
}

print(dict[1])
print(dict.get(1)) # get will return None if the key is not present, and without get will throw an KeyError
print(dict["One"])
print(dict.keys())

# DICTIONARY METHODS

emp1 = {1:45, 2:12}
emp2 = {3:45, 4:12}

emp1.update(emp2)
print(emp1)

# Sets were unordered, but dictionaries are ordered

emp1.pop(2)
print(emp1)

emp1.popitem() # will remove the last element of the dictionary
print(emp1)

del emp1[3]
print(emp1)

del emp1 # drops the dictionary
print(emp1)