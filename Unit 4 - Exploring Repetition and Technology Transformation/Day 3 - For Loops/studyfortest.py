# Example 1: Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# Example 2: Using a condition inside the loop
num = 1
while num <= 10:
    if num % 2 == 0:
        print(num)
    num += 1

# Example 3: Infinite loop with break statement
while True:
    user_input = input("Enter 'ishaan' to abraham: ")
    if user_input.lower() == 'ishaan':
        break
    else:
        print(f'You entered: {user_input}')


# Example 1: Iterating over a list
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    fruit = input("Enter a fruit here: ")
if fruit in fruits:
    print(fruit, "was in the list")
else:
    print("fruit was not in the list")

# Example 2: Using the range function
for i in range(5):
    print(i)

# Example 3: Nested loops
for i in range(3):
    for j in range(2):
        print(f'({i}, {j})')