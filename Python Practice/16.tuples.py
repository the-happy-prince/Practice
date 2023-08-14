tup = (1, 2, 3, 8, 7, 5, 2, 3, 2, 4, 3)
# tup = (1) is considered to be int whereas tup = (1,) is considered to be tuple
print(tup)
print(tup[2])

if 3 in tup:
    print("yes, 3 is present in this tuple")

print(tup.count(3))
print(tup.index(3))
print(tup.index(3, 2, 9)) # slices the tuple from index 2 to 9
print(len(tup))