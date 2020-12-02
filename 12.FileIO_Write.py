file = open("Mayur.txt", "wb")      # "Mayur.txt" -> name of the file which you want to create, "wb" - > write mode
print(file.mode)                    # file will be created in C:\Users\Mayur\PycharmProjects\HelloWorld
print(file.name)

# This is how we write content in the file
file.write(bytes("This file is created by me", "UTF-8"))  # takes two arguments second one is encoding
file.close()
