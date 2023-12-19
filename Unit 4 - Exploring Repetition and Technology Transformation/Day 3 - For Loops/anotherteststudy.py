count = 1
while count <= 7:
    print(count)
    count += 1

correct_password = "python123"
user_input = ""

while user_input != correct_password:
    user_input = input("Enter the password: ")

print("Correct password entered!")

total = 0
num = 2

while num <= 10:
    total += num
    num += 2

print("Sum of even numbers from 2 to 10:", total)

correct_number = 3

while True:
    guess = int(input("Guess a number between 1 and 5: "))
    if guess == correct_number:
        print("Correct guess!")
        break

word = "PYTHON"
index = 0

while index < len(word):
    print(word[index])
    index += 1

for num in range(1, 6):
    print(num)

sum_of_squares = 0
for num in range(1, 5):
    sum_of_squares += num ** 2

print("Sum of squares:", sum_of_squares)

for num in range(3, 13, 3):
    print(num)

for num in range(8, 0, -1):
    print(num)

for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end="\t")
    print()