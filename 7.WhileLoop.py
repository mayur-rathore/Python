print("Enter a number")
number = int(input())

while(number > 4):
    print("Number is greater than 4")
    number = int(input())           # the moment we enter number less than 4 , it will break

print("Enter a number")
no = int(input())

while(no>4):
    print("Number is greater than 4")
    no = int(input())
    if (no == 9):                   # Break the loop when number equals to 9, break exits while loop
        break
    if no == 8:                     # when number equals to 8, execution continue, control goes to while and not print(loop ended)
        continue                    # continue never finish while loop, it start new iteration of while loop
    print("loop ended")
print("Finally came out of while loop")