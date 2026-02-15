# Hashmaps

# Keys are immutable, and the only multi variable structure you could use is a tuple.
# Values are mutable

d = {}
d = dict()

from collections import defaultdict
d = defaultdict(int) # Initializes a default hashmap which allows for unseen keys to be referenced

d[key] = value # Sets value of referenced key
d[key] # Returns value of referenced key
d.values() # returns all values
d.keys() # returns all keys
d.items() # returns all key,value pairs

# Dict comprehension
myMap = { i: 2*i for i in range(3) }
print(myMap)

# Looping through maps
myMap = { "alice": 90, "bob": 70 }
for key in myMap:
    print(key, myMap[key])

for val in myMap.values():
    print(val)

for key, val in myMap.items():
    print(key, val)


# Used for:

# Frequency counting
# Index mapping
# Memoization