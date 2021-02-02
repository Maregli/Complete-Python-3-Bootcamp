########
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

#youn can use %s, %r, .format or formatted string literals (f') to insert formated strings
#for the formatted strings you have to input placeholder brakets {}
age = 22
name = "Michael"
print("I am {}".format(age))
print("My name is {name} and I am {age} years old".format(age = 22, name = "Thomas"))
#to write a float number with a lot of deciamls you can specify the width and precision using: .format(value:width.precision f), width specifies the length of the
#formated strings, but basically it just leads to more or less white space before the string. Width takes into account the length of the string
#so if you write egg and quality with the same width parameter there will be less white space
d = 22.3648449875934
print("this {number:.3f} is a large number".format(number=d))
#you can also format tables like this:
print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:9}'.format('Apples', 3.))
print('{0:8} | {1:9}'.format('Oranges', 10))

#example using f'
print(f"My name is {name} and I am {age} years old") #so you can write variable names directly into the string
#you can pass !r for the string format
print(f"MY name is {name!r}")
#the precision parameter of f is not just for decimals, but the whole string, you can specify it though
num = 45.00
print(f"My 10 character, four decimal number is:{num:10}") #same length but not enough decimals
print(f"My 10 character, four decimal number is:{num:10.4f}")


######
#Lists
######
#Earlier when discussing strings we introduced the concept of a sequence in Python.
#Lists can be thought of the most general version of a sequence in Python. Unlike strings, they are mutable, meaning the elements inside a list can be changed!
my_list = ['A string',23,100.232,'o']
print(len(my_list))
#length will give back the number of items in the list. Nested lists count as one
my_list = ['A string',[23,100.232],'o']
print(len(my_list))
