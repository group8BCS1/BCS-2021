# A program to  be used by the utility company for billing its customers for a certain period of time.
print("==================================================RESTART=======================================================")
# function to calculate the gallons of water used


def gallons(meter_reading1, meter_reading2):
    if meter_reading2 > meter_reading1:
        gallon_of_water = ((meter_reading2 - meter_reading1) / 10)
        print("Gallons of water used:", gallon_of_water)
    else:
        meter_reading1 = 1000000000 - meter_reading1
        gallon_of_water = (meter_reading1 + meter_reading2) / 10
        print("Gallons of water used:", gallon_of_water)
    return gallon_of_water


# function to calculate the amount of money used


def amount_billed():
    code = customer_code
    billed = float()
    if code == "r":
        billed = 5.00 + (gallon * 0.005)
        billed = round(billed, 2)
        print(f"Amount billed:${billed}")
    elif code == 'c':
        if gallon <= 4000000:
            billed = 1000.00
            billed = round(billed, 2)
            print(f"Amount billed:${billed}")
        elif gallon > 4000000:
            billed = 1000.00 + (gallon - 4000000) * 0.00025
            billed = round(billed, 2)
            print(f"Amount billed:${billed}")
    else:
        if gallon <= 4000000:
            billed = 1000.00
            billed = round(billed, 2)
            print(f"Amount billed:${billed}")
        elif 4000000 <= gallon <= 10000000:
            billed = 2000.00
            billed = round(billed, 2)
            print(f"Amount billed:${billed}")
        elif gallon > 10000000:
            billed = 2000.00 + (gallon - 10000000) * 0.00025
            billed = round(billed, 2)
            print(f"Amount billed:${billed}")
    return billed


# main program requesting for value input
beginning_meter_reading = 000000000
ending_meter_reading = 000000000

while True:
    customer_code = input("Enter customer code:").lower()
    beg_meter_reading = int(input("Enter beginning meter reading:"))
    end_meter_reading = int(input("Enter ending meter reading: "))
    if 0 < beg_meter_reading < 999999999 and 0 < end_meter_reading < 999999999:
        if customer_code == "r":
            print("Customer code:", customer_code)
            print(f"Beginning meter reading:{beg_meter_reading:09d}")
            print(f"Ending meter reading:{ end_meter_reading:09d}")
            gallon = gallons(beg_meter_reading, end_meter_reading)
            bill = amount_billed()
            gallon
            bill
        elif customer_code == "c":
            print("Customer code:", customer_code)
            print(f"Beginning meter reading:{beg_meter_reading:09d}")
            print(f"Ending meter reading:{ end_meter_reading:09d}")
            gallon = gallons(beg_meter_reading, end_meter_reading)
            bill = amount_billed()
            gallon
            bill
        elif customer_code == "i":
            print("Customer code:", customer_code)
            print(f"Beginning meter reading:{beg_meter_reading:09d}")
            print(f"Ending meter reading:{ end_meter_reading:09d}")
            gallon = gallons(beg_meter_reading, end_meter_reading)
            bill = amount_billed()
            gallon
            bill
        else:
            print("Invalid code")
    else:
        print("Invalid meter reading")

