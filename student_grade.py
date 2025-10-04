# Program to accept marks and print grade

marks = int(input("Enter the student's marks (0-100): "))

if marks >= 85:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 55:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "Fail"

print("Grade:", grade)


