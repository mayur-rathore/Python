for i in range(0,11):           # it will print numbers from 0 to 10, exclude last index
    print(i)

print('How many times do you want to execute : ')
num = int(input())           # as integer we have to take we did type casting
for i in range(0, num):
    print(i)

# For loop in list format
# Iterate over all the elements of list and then print
list = ['one', 'two', 'three']
for item in list:
    print(item)                # it will print items of list i.e. one, two, three not in row but in next line one by one

# We can also run loop inside loop
list1 = [[1,2,3], [4,5,6], [7,8,9]]
for item1 in list1:
    for i in item1:
        print(i)