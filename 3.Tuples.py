# if we want that our list element will not change in that case we make Tuples

# We make tuples because we don't want to change its elements

tup = (1, 2, 3, 4)         # see the difference here - we are using parenthesis not square brackets like list
print(tup)

print(tup[2])          # it will print 3 according to index

# tup[1] = 9            if we try to change tuple element we get error - "tuple object does not support item assignment"

tup1 = ('Hi', 'how', 'are', 'you')
print(tup1)

# if we want to change anyhow elements of tuples then we need to convert it into List (not recommended)
# and then we can change elements
list1 = list(tup1)      # type casting in list will be done here
print(list1)

# len, max, min functions work same as list in tuples
print(len(tup1))        # length is 4
print(max(tup1))        # max is you because Y is last most alphabet of dictionary
print(min(tup1))        # Hi will be the output

print(len(tup))         # length is 4
print(max(tup))        # max is 4 because 4 is last most
print(min(tup))        # 1 will be the output
