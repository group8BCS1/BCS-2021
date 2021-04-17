# A program that reads an integer from the user representing someones age,
# and decide whether the user can vote or not basing on the age entered.
age = int(input(" Please enter your age! \n"))
print(age)
if age >= 18:
    print("You can vote")
elif age > 0:
    print("Too young to vote")
else:
    print("You are a time traveller")