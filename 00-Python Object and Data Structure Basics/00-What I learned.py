#Numbers
########
a = 10
type(a) #let's you see the type of a variable
########


#Strings
########

#Slicing and Indexing up to a certain point can be done with ":"
b = "Abraham"
print(b[1:5])
print(b[:]) #to grab everything
print(b[:3])

#to slice in a sequence use "::"
print(b[::2]) #to slice in a sequence of two, so every second character
print(b[::-1]) #to write backwards

#strings can be concatenated with +, or multiplied to be printed multiple times

#split strings by a specific character, name of string is before the period
print(b.split("r"))

#to insert formated strings use the .format function, plus you have to insert a placeholder {}, so python knows were to insert the thing
age = 22
name = "Michael"
print("I am {}".format(age))
print("My name is {name} and I am {age} years old".format(age = 22, name = "Thomas"))
#######
