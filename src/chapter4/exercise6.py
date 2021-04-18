#  a function pay computation with time-and-a-half for overtime that takes in two parameters (hours and rate)


def compute_pay(hours, rate):

    if hours <= 40:
        return hours * rate
    else:
        overtime = hours - 40
    return(overtime * 1.5 * rate) + (40 * rate)


duration = int(input("Enter hours worked for; \n"))
pay_per_duration = float(input("Enter the rate; \n"))
payment = compute_pay(duration, pay_per_duration)
print(payment)

