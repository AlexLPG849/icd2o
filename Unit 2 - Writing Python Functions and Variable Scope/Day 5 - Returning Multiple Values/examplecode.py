def sample_function():
    x = 7
    y = 8
    z = 9
    return x, y, z

a, b, c = sample_function()

print(a)
print(c)
print(sample_function())

d = sample_function()
print(d*3)
