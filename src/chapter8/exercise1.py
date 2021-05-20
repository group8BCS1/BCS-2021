#  you can use this to navigate through romeo.txt
# i tried to download the file romeo.txt but failed!
# however that's the code
# Exercise 1

def chop(list):
    fchop = list[1:]
    onumb = len(fchop)
    none = fchop[:onumb-1]
    print(none)
    return none


def middle(mlist):
    newlist = mlist[1]
    nnumb = len(newlist)
    new = newlist[:nnumb-1]
    print(new)
    return new


fruit = ['Mango', 'Orange', 'Pineapple', 'Peach']
print(fruit)

x = chop(fruit)
y = middle(fruit)

if x == y:
    print('Shits identical AND equivalent yo!')
else:
    print('Damn, it\'s equivalent but NOT identical')