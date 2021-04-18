# a program that prompts the user to enter the location and payment
# and then evaluate john's decision to  work
location = input("Enter the city; \n")
payment = int(input(" Enter the payment; \n"))
try:
    location = str(location)
    payment = int(payment)
    if location == "space":
        print("Without a doubt i will take it")
    elif location == "Mbarara":
        if payment > 4000000:
            print("I can work there ")
        else:
            print("No thanks i can find something better ")
    elif location == "Kampala":
        if payment >= 10000000:
            print("Sure i can work with this ")
        else:
            print("No way ")
    else:
        if payment >= 6000000:
            print("This is fine I can work with you ")
        else:
            print("I can find something better")
except :
    print("Enter numerical payment and a city")