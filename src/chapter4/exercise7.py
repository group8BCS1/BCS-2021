# A program that uses a function called computer_grade, takes score as its parameter.
# returns a grade as a string and computes the grade of the score
def computer_grade(score):
    if score >= 0.0 and score <= 1.0:
        if score >= 0.9:
            return 'A'
        elif score >= 0.8:
            return 'B'
        elif score >= 0.7:
            return 'C'
        elif score >= 0.6:
            return 'D'
        elif score < 0.6:
            return 'F'
    else:
        return 'Bad score'


mark = float(input("Enter your score; \n"))
grade = computer_grade(mark)
print("Your grade is", grade)


