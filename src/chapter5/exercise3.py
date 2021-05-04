# this is an exercise3 for group8BCS1
# GROUP 8 BCS1 MEMBERS INCLUDE
# Ndagire Lillian 2020/BCS/007
# Kirumira Eric 2020/BCS/071/PS
# Arinjuna Sarah 2020/BCS/093/PS
# Siemba Ernest Ooko 2020/BCS/005
# 25th April 2021
# a program for the vending machine that dispenses the change after purchasing products
# Stock
def alg(bal):
    while bal > 0.25:
        print(bal//0.25, 'quarters')
        bal = bal % 0.25
        continue
    while bal > 0.1:
        print(bal//0.1, "dimes")
        bal = bal % 0.1
        continue
    while bal > 0.05:
        print(bal//0.05, "nickels")
        break
    else:
        print("0 cents")


# function to give change
def change(total_deposit, price1):
    bal = total_deposit - price1
    print("Take the change below:")
    alg(bal)


# function that converts money into dollars and cents
def money(price1):
    dollar = price1 // 1
    cents = price1 % 1
    # print(cents)
    # print(dollar)
    if dollar == 0:
        print("Payment due:", round(cents * 100), "cents")
    else:
        print("Payment due:", round(dollar), "dollars and ", round(cents * 100), "cents")


# Function to request for deposit
def deposit():
    total_deposit = 0
    pric = price1
    while total_deposit < price1:
        dep = input("Indicate your deposit:")
        if dep == 'c':
            print("Take the change below")
            change(total_deposit, 0)
            break
        elif dep == "f":
            total_deposit = total_deposit + 5
            pric = pric - 5
            if total_deposit < price1:
                money(pric)
            else:
                change(total_deposit, price1)
        elif dep == 'o':
            total_deposit = total_deposit + 1
            pric = pric - 1
            if total_deposit < price1:
                money(pric)
            else:
                change(total_deposit, price1)
        elif dep == 'q':
            total_deposit = total_deposit + 0.25
            pric = pric - 0.25
            if total_deposit < price1:
                money(pric)
            else:
                change(total_deposit, price1)
        elif dep == 'd':
            total_deposit = total_deposit + 0.1
            pric = pric - 0.1
            if total_deposit < price1:
                money(pric)
            else:
                change(total_deposit, price1)
        elif dep == 'n':
            total_deposit = total_deposit + 0.05
            pric = pric - 0.05
            if total_deposit < price1:
                money(pric)
            else:
                change(total_deposit, price1)
        else:
            print("Illegal selection:", dep)


# main program
print("Welcome to te vending machine change maker program")
print("Change maker initialized")
# Stock contains:
nickels = 25
dimes = 25
quarters = 25
ones = 0
fives = 0
print("stock contains:")
print(nickels, "nickels")
print(dimes, "dimes")
print(quarters, "quarters")
print(ones, "ones")
print(fives, "fives")
while True:
    try:
        price = input("Enter price or quit:")
        if price == "q":
            print("quit")
            break
        price1 = float(price)
        if price1 > 0 and (price1*100) % 5 == 0:
            print("Deposit menu")
            print("""'n' - deposit a nickel
            'd'- deposit a dime
            'q'- deposit quarters
            'o'- deposit one dollar bill
             'f'- deposit a five dollar bill
             'c'- cancel purchase""")
            money(price1)
            deposit()
        else:
            print("price entered should be a multiple of 0.05 and non negative number ")


    except:
        print("Invalid input")
        continue

