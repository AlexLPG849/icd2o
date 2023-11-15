x = 5
y = 10

# Using 'and' to check multiple conditions
if x > 0 and y > 0:
    print("Both x and y are greater than 0")

# Using 'or' to check multiple conditions
if x > 0 or y > 0:
    print("At least one of x or y is greater than 0")

# Using 'not' to negate a condition
if not x > 10:
    print("x is not greater than 10")

# Combining 'and', 'or', and 'not' for more complex conditions
if (x > 0 and y > 0) or not x > 10:
    print("x and y are both greater than 0 OR x is not greater than 10")