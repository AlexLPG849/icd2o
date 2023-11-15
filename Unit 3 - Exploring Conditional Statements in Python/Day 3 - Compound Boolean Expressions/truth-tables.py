# Truth table for AND
print()
print("A\tB\tA AND B")
for A in [True, False]:
    for B in [True, False]:
        result = A and B
        print(f"{A}\t{B}\t{result}")

print()
# Truth table for OR
print("A\tB\tA OR B")
for A in [True, False]:
    for B in [True, False]:
        result = A or B
        print(f"{A}\t{B}\t{result}")



print()
# Truth table for NOT
print("A\tNOT A")
for A in [True, False]:
    result = not A
    print(f"{A}\t{result}")