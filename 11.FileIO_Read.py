# This is how we read the file - use mode "r+" to read the file
file = open("Mayur.txt", "r+")
text_to_read = file.read()
print(text_to_read)