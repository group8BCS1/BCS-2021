# Programme that reads user input and prints the final value of investment
c = int(input(" Enter initial amount of invest: \n"))
r = float(input("Enter the yearly rate of interest: \n"))
n = int(input("Enter number of times the interest is compounded per year: \n"))
t = int(input("Enter the number of years until maturity: \n"))
tn = t * n
p = c * (1 + r/n)**tn
print(round(p, 2))

p = c * ( 1+ r/n)**tn
print( round (p,2))
print(p)

