# A program that takes in function investment that take in c r t  and n
# and calculates the final amount  of investment
# pay = c(1 + (r/n))**(t * n)
def final_investment(c, r, t, n):
    pay = c*((1 + (r/n))**(t * n))
    return pay


initial_value = input("Enter initial value of investment; \n")
rate = input("Enter the rate; \n")
number_of_times = input("Enter the number of times the interest has to be compounded; \n")
time = input("Enter the years; \n")
try:
    initial_value = int(initial_value)
    rate = float(rate)
    number_of_times = int(number_of_times)
    time = int(time)
except:
    print("enter numeric")
    quit()

p = final_investment(initial_value, rate, time, number_of_times)
print(round(p, 2))
