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
#so if you write egg and quality with the same width parameter there will be less white space. precision is decimals
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

#Lists can be expanded/multiplied just like strings, either with + or *
#to add an item permanently to a list you could either
my_list=my_list+["permanent item 1"] #or
my_list.append("permanent item 2")
print(my_list)

#to remove an object use pop function, specify the index, default is last item
my_list.pop(4)
print(my_list)

#you can also sort (alphabetically, or with numbers ascending) and reverse a list, this is changes original list directly
#my_list.sort() this doesn't work because list has different types of items, only works with pure int or pure str lists
#print(my_list)
alpha_list = ["b", "d", "la", "g"]
alpha_list.sort()
print(alpha_list)

#nesting lists, you can nest lists and with [][] you can call on an item inside a nested list like this:
my_list2 = [1,2,3,4,5]
#if you don't want them nested
matrix = my_list+my_list
print(matrix)
#nested format:
matrix = [my_list, my_list2]
print(matrix)
#call on specific items by stacking the brackets:
print(matrix[0][1][1])

#######
#Dictionaries
#######
#Unlike sequences (like lists or strings), dictionaries are mappings, which means that the objects in a dictionary
#are stored by a key and not their position in the sequence. dictionary consists of key and value assigned to it

my_dict = {"Mike": {"age":22, "gender":"male", "height":1.90}, "Sara": {"age":23, "gender":"non-binary", "height":1.63}}
print(my_dict["Mike"]["height"])
print(f'{my_dict["Mike"]["height"]:.2f}') #for some reason I can't use them same quotation marks for the f function
#and the keys. Maybe because f is a function
#add keys and values (similar to r where you make a new variable)
my_dict["Thomas"] = "male"
print(my_dict)

#dictionary functions
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())#this creates tuples from the key and value pairs

#######
#Tupples
#######
#kinda like Lists (can mix objects), but immutable. Use for things of which order mustn't be changed
#tuples are created with ()
t = (1,2,3, "shelf")
print(len(t))
print(t[-1])
print(t.count(2))
#use.index to type in a value and get back the index
print(t.index("shelf"))
#you can neither add to tupples, nor change their values. They are immutable!!

########
#Sets
######
#sets are an unordered collection of UNIQUE Elements
x = set()
#instead of using append like in lists, we use add to add stuff
x.add("Gucci")
x.add("Prada")
print(x)
#you cannot add a value to a set, if it is already in the set:
x.add("Prada")
print(x)
#to extract unique values of a list, you can create a set based on the list:
lyst_trial = [1,2,1,1,1,2,3,4,2,2,1,2,3,5]
print(set(lyst_trial))

#######
#Booleans
#######
#basically these are True/False Vectors
#there is also placeholder object none

#######
#Files
######
# These operators to specify open function so that you can write/read document/text file
# "r"   Opens a file for reading only.
# "r+"  Opens a file for both reading and writing.
# "rb"  Opens a file for reading only in binary format.
# "rb+" Opens a file for both reading and writing in binary format.
# "w"   Opens a file for writing only.
# "a"   Open for writing.  The file is created if it does not exist.
# "a+"  Open for reading and writing.  The file is created if it does not exist.
import os
print(os.getcwd())
dir_path = os.path.dirname(os.path.realpath("test1.txt"))
print(dir_path)
# file = open("test1.txt", "a+")
# file.write("This is the first line\nthis is the second line")
# file.close()
# file = open("test1.txt", "r")
# print(file.read())


