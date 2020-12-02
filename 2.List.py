#List

colleges = ["IIT", "NIT", "MIT", "College of engineering"]
print(colleges)

print(colleges[2])

colleges[3] = "COE"
print(colleges)

print(colleges[1:4])        # start from index 1 and goes up to 1,2 and 3 i.e. exclude last index i.e. 4

list2 = ['table', 'chair', 'fan', 'microphone', 'bottle']
list2.insert(3, 'clothes')      # insert takes two arguments, first is index and second is value
print(list2)

list2.remove("fan")             # to remove any element in the list
print(list2)

print(list2 + ["pillow", "tube light", "bed"])  # by using '+' sign we can add the list

print(len(list2))               # length will be 5, + just add elements in the list not change the size of list
print("maximum of list2 is ", max(list2))       # output will be table i.e. last alphabet in dictionary is 't'
print("minimum of list2 is ", min(list2))       # output will be bottle i.e. first alphabet in dictionary among the list is 'b'

