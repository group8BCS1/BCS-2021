#A programm that breaks down money entered by the user
amount = float(input("Enter amount to be changed; \n"))
print("Your change is ...... \n")
print(amount//20, "twenties")
amount = amount % 20
print(amount//10, "tens")
amount = amount % 10
print(amount//5, "fives")
amount = amount % 5
print(amount //1, "ones")
amount = amount % 1
print(amount // 0.25, "quaters")
amount = amount % 0.25
print(amount //0.1, "dime")
amount = amount % 0.1
print(amount // 0.05, "nickel")
amount = amount % 0.05
print(amount //0.01, "penny")