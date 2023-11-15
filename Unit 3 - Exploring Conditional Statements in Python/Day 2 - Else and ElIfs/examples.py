num = int(input("Please enter a number here: "))

if num >= 10:
    print(True)
if num < 10:
    print(False)

number_grade = 76
if number_grade >= 80:
    print("A")
if 70 <= number_grade < 80:
    print("B")
if 60 <= number_grade < 70:
    print("C")
if 50 <= number_grade < 60:
    print("D")
if number_grade < 50:
    print("F")


if number_grade >= 80:
    print("A")
elif number_grade >= 70:
    print("B")
elif number_grade >= 60:
    print("C")
elif number_grade >= 50:
    print("D")
elif number_grade < 50:
    print("F")


if number_grade >= 80:
    print("A")
elif number_grade >= 70:
    print("B")
elif number_grade >= 60:
    print("C")
elif number_grade >= 50:
    print("D")
else:
    print("F")

def inspect_number(x):
    if x > 0:
        print("Positive")
    elif x < 0:
        print("Negative")
    else:
        print("Zero")

inspect_number(14)
