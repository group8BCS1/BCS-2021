# a program   that repeatedly reads numbers from the user
# calculates the total, count and the average . use try and except to detect mistakes from the user
count = 0
total = 0
average = 0
while True:
    try:
        numeric = input("Enter a number;")
        if numeric == "done":
            break
        numeric = int(numeric)
        count = count + 1
        total = total + numeric
        average = total / count
    except:
        print("invalid input")
print("Total=", total)
print("Count=", count)
print("Average =", average)






