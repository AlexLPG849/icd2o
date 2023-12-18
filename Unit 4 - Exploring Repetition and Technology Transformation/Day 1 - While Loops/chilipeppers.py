num_peppers = int(input())
count = 0
total = 0

while count<num_peppers:
    pepper = input()
    if pepper == "Poblano":
        total == 1500
    elif pepper == "Mirasol":
        total += 6000
    elif pepper == "Serrano":
        total += 15000
    elif pepper == "Cayenne":
        total += 40000
    elif pepper == "Thai":
        total += 75000
    elif pepper == "Habanero":
        total += 125000

    
    count+=1

print(total)