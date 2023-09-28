age = 40
name = "Abrnam"

print("Name: " + name + ". Age: " + str(age))
# works but we need + everywhere and we keep opening and closing strings
# we have to change everything into a String using str()

# the other option is to use f-string(formatted strings)
print(f"Name: {name}. Age: {age} years.")

