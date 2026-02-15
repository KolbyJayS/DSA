# Tuples

# Tuples are like arrays but immutable
tup = (1, 2, 3)
print(tup)
print(tup[0])
print(tup[-1])

# Can be used as key for hash map/set
myMap = { (1,2): 3 }
print(myMap[(1,2)])

# Also can use within a hashset
mySet = set()
mySet.add((1, 2))
print((1, 2) in mySet)