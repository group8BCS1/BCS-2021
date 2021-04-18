# a pay program that uses try and except to handle non numerical input
# and prints out the program
hours = input('Enter hours: \n')
try:
    hours = int(hours)
    rt = input("Enter Rate:")
    rate = float(rt)
    pay = hours * rate
    if hours <= 40:
        print(pay)
    else:
        pay_above_40 = (40 * rate + (hours - 40) * 1.5 * rate)
        print(pay_above_40)
except:
    print(" enter numeric input")
