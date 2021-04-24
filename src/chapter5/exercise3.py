# this is an exercise3 for group8BCS1
#     GROUP 8 BCS1 MEMBERS INCLUDE
#     Ndagire Lillian 2020/BCS/007
#     Kirumira Eric 2020/BCS/071/PS
#     Arinjuna Sarah 2020/BCS/093/PS
#     Siemba Ernest Ooko 2020/BCS/005
# a program for the vending machine that dispenses the change after purchasing products
# Stock
def money(price1):
    dollar = price1 // 1
    cents = price1 % 1
    print(cents)
    print(dollar)


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
        if price1 > 0 and price1 % 0.05 == 0:
            print("Deposit menu")
            print("""'n' - deposit a nickel
            'd'- deposit a dime
            'q'- deposit quarters
            'o'- deposit one dollar bill
             'f'- deposit a five dollar bill
             'c'- cancel purchase""")
            money(price1)
        else:
            print("price entered should be a multiple of 0.05 and non negative number ")


    except:
        print("Invalid input")
        continue

