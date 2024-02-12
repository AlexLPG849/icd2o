list = [3,8,35,49,843,12903,934443,9023904,23329820]
print(list)
for element in list:
    print(element)
total = 0
for el in list:
    total += el
print(total)
print(sum(list))
print("Positive Even Numbers:")
for el in list:
    if el % 2 == 0 and el > 0:
        print(el)
smallest = list[0]
for el in list:
    if el < smallest:
        smallest = el
print("Smallest Number in List:")
print(smallest)
biggest = list[0]
for el in list:
    if el > biggest:
        biggest = el
print("Biggest Number in List:")
print(biggest)
print("Using min and max:")
print(min(list))
print(max(list))
print("Using words:")
name_list = ["ishaan", "alexander", "abraham", "brandon"]
biggest_name = name_list[0]
for el in name_list:
    if el > biggest_name:
        biggest_name = el
print(max(name_list))
print("Finding longest name in length")
longest = name_list[0]
for el in name_list:
    if len(longest) < len(el):
        longest = el
print(longest)
print(max(name_list,key=len))