#1
wins = int(input("Enter your wins in a number here: "))
if wins >= 5:         
    print(f"you are in group {1}")     
elif wins >= 3:         
    print(f"you are in group {2}")    
elif wins >= 1:        
    print(f"you are in group {3}")   
else:         
    print(f"you are eliminated from the tournament (-1)")  

#2
sample = input()

row1 = sample.split()
row2 = sample.split()
row3 = sample.split()
row4 = sample.split()


sum = 0
for i in range(4):
    sum += int(row1[i])

print(sum)

sum1 = 0
for j in range(4):
    sum1 += int(row2[j])

print(sum1)

sum2 = 0
for k in range(4):
    sum2 += int(row3[k])

print(sum2)

sum3 = 0
for l in range(4):
    sum3 += int(row4[l])

print(sum3)