# Check if a number is positive.
number = 89
if number > 0:
    print(f"{number} is positive")
if number <= 0:
    print(f"{number} is not positive")


# Determine if a person can vote (age 18 or older).
num = int(input("Please enter your age: "))
if num >= 18:
    print(f"You are eligible to vote.")
if num <= 18:
    print(f"You are underage to vote")


# Check if a string is empty.
str = input("Please enter a string: ")
if len(str) == 0:
    print(f"The string is empty")
if len(str) != 0:
    print(f"The string is not empty")


# Determine the maximum of two numbers.
def max_numbers(a, b):
    if a > b:
        return a
    
    return b
print(max_numbers(4, 5))
print(max_numbers(14, 5))


# Check if a user's input is equal to a secret password.
def password_checker(password, user_input):
    if password == user_input:
        return True
    
    return False
pwd = input("Password: ")
secret = "BV78q9b7GBU6ggb79"
print(password_checker(secret, pwd))


# Write a function that checks if a number is within a specific range.
def range_checker(num, lower, upper):
    if lower <= num <= upper:
        return True
    
    return False

a = int(input("Please enter a number between 1 and 10: "))
if range_checker(a, 1, 10):
    print("Good you listen to instructions!!!")
if range_checker(a, 1, 10) == False:
    print("ARGHH!!! I am not happy because you don't listen!!!")




# Write a function that accepts a numberical grade and returns the Letter Grade

def grade_converter(grade):
    if grade >= 80:
        return "A"
    if grade >= 70:
        return "B"
    if grade >= 60:
        return "C"
    if grade >= 50:
        return "D"
    if grade <= 49:
        return "F"