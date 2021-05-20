
# Exercise 4
words = []
fhand = open('romeo.txt', 'r')
for line in fhand:
    for word in line.split(' '):
        if word not in words:
            words.append(word)
print(sorted(words))



