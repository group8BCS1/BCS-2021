# a program   of looping and counting  function that takes int two parameters word and letter
# and prints times a letter appears int he word takes in word a
def count(word, letter):
    let_count = 0
    for lette in word:
        if lette == letter:
            let_count += 1
    print(let_count)


word = input("Enter a word ")
letter = input("Enter a letter ")
test = word.count(letter)
print(test)
