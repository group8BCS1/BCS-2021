# a program that prompts for  list of  numbers from the user
# and prints out both maximum and minimum number
count = 0
total = 0
numbers = list()
while True:
    try:
        numeric = input("Enter a number;")
        if numeric == "done":
            break
        numeric = int(numeric)
        numbers.append(numeric)
        count = count + 1
        total = total + numeric
        maximum_number = max(numbers)
        minimum_number = min(numbers)
    except:
        print("Invalid input")
print("Count", count)
print("Total = ", total,)
print("Maximum  number= ", maximum_number)
print("Minimum number = ", minimum_number)
