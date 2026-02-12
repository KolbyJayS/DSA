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


# Used for:

# Frequency counting
# Index mapping
# Memoization


# HashSets

# Can't have duplicates. Like a Hashmap but only the keys.

s = set() # Initializes a hashset
s.add(x) # adds x element to hashset s
s.remove(x) # removes x element from hashset s
x in s # returns boolean if element x is in hashset s