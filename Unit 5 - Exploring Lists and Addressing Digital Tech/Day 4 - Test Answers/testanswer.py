n = int(input("Please enter a positive number: "))
while n <= 0:
    break

import random
number = random.randint(1,10)
guess = 0
while guess != number:
    guess = int(input("Enter your guess: "))
    if guess < number:
        print('Too low')
    elif guess > number:
        print('Too high')
    else:
        print('Correct')

num = 2
sums = 0
while num <= 10:
    sums += num
    num += 2

print(sums)
##############################################################
sumi = 0
for i in range(1,21):
    if i % 2 == 0:
        sumi += 1

print(sumi)

letter = input("Please enter a letter: ")
numero = int(input("Please enter a number: "))
result = ''
for i in range(1, numero+1):
    result += letter
    result = result + letter
print(result)

for i in range(8,0,-1):
    print(i)

def count_vowels(str):
    num_vowels = 0
    vowels = "aeiou"
    for i in range(len(str)):
        if str[i] in vowels:
            num_vowels += 1
        return num_vowels
    
def reverse_string(str):
    results = ''
    for i in range(len(str)-1,-1,-1):
        result += str[i]
    return result

def remove_vowels(str):
    result = ''
    vowels = "aeiou"
    for i in range(len(str)):
        if str[i] not in vowels:
            result += i
        return result