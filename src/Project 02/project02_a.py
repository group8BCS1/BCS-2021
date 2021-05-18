out = input("Enter out put file: ")
user = input("Enter a year: ")
if user == "":
    with open("measles.txt", "r") as main_file:
        with open(out, "w") as output:
            for line in main_file:
                output.write(line)

elif user == "all":
    with open("measles.txt", "r") as main_file:
        with open(out, "w") as output:
            for line in main_file:
                output.write(line)

elif user == "ALL":
    with open("measles.txt", "r") as main_file:
        with open(out, "w") as output:
            for line in main_file:
                output.write(line)
elif user.isdigit():
    with open("measles.txt", "r") as main_file:
        with open(out, "w") as output:
            for line in main_file:
                year = line[-5:]
                if year.startswith(user):
                    output.write(line)
else:
    print("Invalid input please enter a valid response:")