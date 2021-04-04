# An algorithm that prompts the user for the number of people attending their wedding
# and prints the catering costs
Guests = input("Enter number of guest attending your wedding: \n")
try:
    Guests = int(Guests)
    if Guests <= 50:
        print("The wedding costs $4000")
    elif Guests <= 100:
        print("The wedding costs $10,000 ")
    elif Guests <= 200:
        print("The wedding costs $15,000")
    else:
        print("The wedding costs $20,000")
except:
    print("Enter number of guests numerically")