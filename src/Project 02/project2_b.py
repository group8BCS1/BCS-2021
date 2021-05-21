# This function opens the file and returns a file object
def open_file():
    while True:
        main_file = input("Enter file name: ")
        try:
            file_ = open(main_file, 'r')
            break
        except:
            print("Invalid file name, please enter correct file name!")
    return file_


def process_file(open_object):  # """This function processes the file"""
    try:
        low_income = 'WB_LI '
        lower_middle_income = 'WB_LMI'
        upper_middle_income = 'WB_UMI'
        high_income = 'WB_HI '
        year = input("Enter Year: ")
        income_level_display = """
        1 - Low income
        2 - Lower middle income
        3 - upper middle income
        4 - high income 
        """
        income_level = input(f"{income_level_display} \nEnter income Level: ")
        count = 0
        total = 0

        # lists to store countries and percentages
        countries = []
        percentages = []

        for line in open_object:
            if year == line[88:92]:  # finding the year at the specific index
                if income_level == '1':
                    if line[51:57] == low_income:
                        percent = float(line[58:61])
                        count += 1
                        total += percent
                        countries.append(line[0:49].strip())  # adding  the country to the list
                        percentages.append(percent)  # adding the percentage got to the list
                        continue
                elif income_level == '2':  # for lower_middle_income income
                    if line[51:57] == lower_middle_income:
                        percent = float(line[58:61])
                        total += percent
                        count += 1
                        countries.append(line[0:49].strip())
                        percentages.append(percent)
                        continue
                elif income_level == '3':  # for upper_middle_ income
                    if line[51:57] == upper_middle_income:
                        percent = float(line[58:61])
                        count += 1
                        total += percent
                        countries.append(line[0:49].strip())
                        percentages.append(percent)
                        continue
                elif income_level == '4':  # for high income
                    if line[51:57] == high_income:
                        percent = float(line[58:61])
                        count += 1
                        total += percent
                        countries.append(line[0:49].strip())
                        percentages.append(percent)
                        continue
        print(f'There are {count} countries found')
        print(f'The average is {round(total / count, 1)}')
        print("")
        # getting the highest and lowest  percentage
        max_value = max(percentages)
        min_value = min(percentages)

        oxford = dict(zip(countries, percentages))
        mx = [k for k, v in oxford.items() if v == max_value]
        mn = [k for k, v in oxford.items() if v == min_value]
        print(f"The following have the maximum value of {max_value}")
        for i in mx:
            print(i)
        print(f"The following have the minimum value of {min_value}")
        for i in mn:
            print(i)
    except:
        print("Invalid Inputs")


def main():  # """This func calls the open_file function and process_file function"""
    user_file = open_file()
    process_file(user_file)


main()  # invoking the main function
