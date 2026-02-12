# Strings

# Essentially an array of chars

s = "" # Default Initialize
s = "abc" # Value Initialize
s = str(123) #Explicit conversion of integer 123 into string "123"

s[i]   # Returns char at given index
s[-1]  # Returns last char in string             
s[l:r] # Splicing. Returns chars between l and r index.
len(s) # Returns Length of string

s.lower() # Makes string all lowercase
s.upper() # makes string all uppercase
s.isalnum() # returns boolean of if string is all alphanumerical
s.isalpha() # returns bool of if string is all alphabetical
s.isdigit() # returns bool of if string is all numerical
s.strip() # Removes leading or trailing character matching given element
s.split() # Breaks string into list of substrings given a delimiter
s = " ".join(list_of_strings) # Joines list of strings together
s.replace(old, new) # Returns string where all occurences of substring old is replaced by new


