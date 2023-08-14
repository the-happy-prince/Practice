sets = {2, 4, 2, 6}
print(sets)
# Does not allow duplicates

info = {"Prince", 22, False, 6.7}
print(info) 
# There is no guarentee about the order of the elements

setordict = {} # This is a dictionary, not an empty set
setordict = set() # This is an empty set


#--------------------------------------------------------------------#
# SET METHODS
#--------------------------------------------------------------------#\

s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
print(s1.issubset(s2))
print(s1.issuperset(s2))
print(s1.isdisjoint(s2))