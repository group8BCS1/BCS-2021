# Part A of the program that  copies lines selected by the user from measles.txt file to the output file
file = input("Enter out put file: ")
if '.txt' in file:
    pass
else:
    print("invalid output file")
    exit()
user = input("Enter a year: ")
if user == "":  # for "" and the  copies everything to the output file
    with open("measles.txt", "r") as main_file:
        with open(file, "w") as output:
            for line in main_file:
                output.write(line)

elif user == "all":  # for all and the  copies everything to the output file
    with open("measles.txt", "r") as main_file:
        with open(file, "w") as output:
            for line in main_file:
                output.write(line)

elif user == "ALL":  # for all and the  copies everything to the output file
    with open("measles.txt", "r") as main_file:
        with open(file, "w") as output:
            for line in main_file:
                output.write(line)
elif user.isdigit():  # entering a digit
    with open("measles.txt", "r") as main_file:
        with open(file, "w") as output:
            for line in main_file:
                year = line[-5:]  # taking character from index -4 onwards
                if year.startswith(user):  # allowance for all full year and its prefixes
                    output.write(line)
else:
    print("Invalid input please enter a valid response:")
