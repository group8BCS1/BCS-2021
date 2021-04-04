# A program to prompt for a score between 0.0 to 1.0 from the user and gives a grade
score = float(input("Enter your score \n"))
try :
    score = float(score)
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    elif score < 0.6:
        print("F")
except :
    print("Bad score")