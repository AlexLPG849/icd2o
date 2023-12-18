def example_one():
    for count in range(10) :
        print(count + 1)
example_one()

def example_two():
    for counter in range(2, 12, +2):
        print(counter)
example_two()

def example_three():
    sum = 0
    for i in range(1, 9, +2):
        sum += i
    print(sum)
example_three()

def example_four():
     for i in range(10, 0, -1):
        print(i)
example_four()

def example_five():
    for i in range(4, 21, 4):
        print(i)
example_five()

def example_six():
    product = 1
    for i in range(1, 6):
        product *= i
        print(product)
example_six()

def example_seven():
    for i in range(3, 15):
        if i % 3 == 0:
            print(i)
example_seven()

def example_eight():
    for i in range(5, 0, -1):
        print(i)
    print("Blast Off!!!")
example_eight()

def example_nine():
    for i in range(1, 6):
        print(i*i)
example_nine()

def example_ten():
    for n in range(1, 8):
        product = 1
        for i in range(n, 0, -1):
            product*=i
        print(product)
example_ten()

def example_eleven():
    str = "WONDERFUL"
    for i in range(1,len(str),2):
        print(str[i])
example_eleven()

str = "COMPUTER".lower()

counts = 0
for index in range(len(str)):
    if str[index] in ('a', 'e', 'i', 'o', 'u'):
        counts += 1
print(counts)

normal = "RACECAR"
backwards= ""


for index in range(len(normal)-1, -1, -1):
    backwards += normal[index]
    
if backwards == normal:
    print("Yes it is a palindrome")
else: 
    print('No it is not a palindrome')