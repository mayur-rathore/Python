# Dictionaries helps us in representing key value pair

# let say i have to store age of peoples with their name in one data type, then i can make a dictionary

# Use curly braces for dictionary, square bracket for list, parenthesis for tuples
names = {
            "abc": 27,
            "def": 89,
            "pqr": 45,
            "qwe": 34
        }

print(names)
print(names["pqr"])     # it will print age of pqr i.e. print value of given key
names["pqr"] = 753      # this is how we can update any value
print(names)
print(names["pqr"])

# If at any point of time you forgot about your keys, you can print you keys and also values but values may change you
# will get latest ones
print(names.keys())
print(names.values())
