age = 25
name = "Jack"
shoe_size = 9.5

# variable names can only be text, number and underscores
# 8shoe_size  cannot start with a number
# _shoe_size = 7.6  we can start with an underscore but try not to

# print(name +" is " + age +"years old"+ name + "wears a shoe size of" + shoe_size + "shoe")
# We are expecting:
# Jack is 25 years old. Jack wears a size 9.5 shoe.
# We got: TypeError: can only concatenate str (not "int") to str
# concatenate means to join together
# It is saying we cannot joni strings and integers together

print(str(name) +" is " + str(age) +" years old. "+ str(name) + " wears a shoe size of " + str(shoe_size) + " shoe.")
# complete (Jack is 25 years old. Jack wears a shoe size of 9.5 shoe.)

# Let's choose the naming convention for variables as all_lower_case with underscore for spaces
