# HashSets

# Can't have duplicates. Like a Hashmap but only the keys.

s = set() # Initializes a hashset
s.add(x) # adds x element to hashset s
s.remove(x) # removes x element from hashset s
x in s # returns boolean if element x is in hashset s
newSet = set([1, 2, 3]) # List to set

# Set comprehension
mySet = { i for i in range(3) }
print(mySet)