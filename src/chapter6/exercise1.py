# A program that prints a word from the  last character back to the first on the separate line
word = input("Enter a word ")
index = -1
while index > -(1+len(word)):
    print(word[index])
    index -= 1
