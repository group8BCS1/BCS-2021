# easter egg program for a file name na na boo
file = input("Enter file name: ")
try:
    if file == "na na boo":
        print("NA NA BOO BOO TO YOU- you have been punk'd!")
    else:
        count = 0
        file_name = open(file)
        for line in file_name:
            if line.startswith("Subject"):
                count += 1
        print("There were ", count, "subject line", file)
except FileNotFoundError:
    print("File cannot be opened:", file)

