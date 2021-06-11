# a program that open and reads words in  words.txt and translates them into a dictionary items as key_values
file = input("Enter file name: ")
handle = open(file, 'r')
handle_file = dict()
for line in handle:
    words = line.split()
    for word in words:
        handle_file[word] = handle_file.get(word, 0) + 1
print(handle_file)