# A program that reads through the file and prints the contents of the file line by line.

file = open(input("Enter the file name: "))
file_name = file.read()
for line in file_name:
    print(line.upper(), end=" ")
