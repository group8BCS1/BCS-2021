# A program that takes in function investment that take in c r t  and n
# and calculates the final amount  of investment
# p = c(1 + (r/n))**(t * n)
def final_investment(c, r, t, n):
    first = (1 + r/n)
    sec = first**(t * n)
    final = c * sec
    return round(final, 2)


initial_value = 1000
rate = 0.01
times_interest_is_comp = 1
time = 1
p = final_investment(initial_value, rate, time, times_interest_is_comp)
print(p)
