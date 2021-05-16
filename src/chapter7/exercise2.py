# A program that prompts for file name from the user and reads through the files
# and reads line of form "X-DSPAM-Confidence:0.8475
try:
    confidence_list = []  # list to collect extracted numbers
    file_name = open(input("Enter the file name: "))
    count = 0
    for line in file_name:
        if line.startswith('X-DSPAM-Confidence:'):
            first = (line.find(":"))  # finding where the ":" is located
            extract = float(line[first+1:])  # extracting characters immediately after the ":" till the end
                                              # and changing to a float
            confidence_list.append(extract)  # adding the new number got to a list
            count += 1
    print("average confidence", sum(confidence_list)/count)  # getting the average
except:
    print("file doesnt exist")




