# To get input from user in python - use input

# Problem with input is it accepts String input only
# to convert it into int we need to typecast
number = input("please enter the number : ")
print(number)

# if user want to take integer input then typecast
number = int(input("please enter the number : "))
print(number)

# Indentation refers to the whitespaces (usually 4 spaces or a single tab) at the beginning of a code line.
# Python uses indentation to indicate a block of code.
# Python will give an error if we skip the indentation.
# The number of spaces is up to you as a programmer, but it has to be at least one.
# We have to use the same number of spaces in the same block of code, otherwise Python will give an error:

print('please enter marks of student')
number = int(input())           # as we are dealing in integers we have to typecast it

if (number > 90 and number < 100):      # if we enter marks more than 100 then issue, hence use and
    grade = 'A'
elif (number > 80 and number < 100):
    grade = 'B'
elif (number > 40 or number < 45):
    grade = 'D'
else:
    grade = "don't know"
print("grade of student is :", grade)