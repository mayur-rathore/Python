string1 = "This is me"
print(string1[1:3])     # starts from first index and continue till last index-1 i.e. 3-1 second index

print(string1[-4:])     # means count from last and get 4 characters output = s me
print(string1[-5:])     # output = is me
print(string1[:-3])     # remove last 3 characters and get everything output =  This is
print(string1[:-1])     # remove last 1 character and get everything output = This is m

string2 = 'hi i am good'
print(string2.capitalize())         # make first character of string capital output = Hi i am good
# we will get index using find from where give character is starting
print(string2.find("am"))           # output =5 , am is starting from index 5
print(string2.find("good"))         # output =8 , good is starting from index 5
print(string2.find("ghjdf"))        # output = -1, shows string is not available

# use replace function carefully, because it replace all instances of given string
print(string1.replace("is", "are"))     # output = Thare are me, replace all is in the string with are

