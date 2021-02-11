######
#If, Elif, Else
########

#The first form if-if-if tests all conditions, whereas the second if-elif-else tests only as many as
# needed: if it finds one condition that is True, it stops and doesn't evaluate the rest. In other words: if-elif-else
# is used when the conditions are mutually exclusive.


########
#For loops
########

#for loop acts as an iterator in Python; it goes through items that are in a sequence or any other iterable item
#for loop to print even numbers from 1 to 10
for num in range(1,10):
    if num % 2 == 0:
        print(num)
#instead of range you could also use any other sequence, like a string:
#notic print parameters: print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False),
#if file is not specified, it will print it on screen. end is default new line
a = "This is a string"
for i in a:
    print(i, end="")
print("\n")

#loop through list:
lis = [1,2,"abc", [3,4]]
for i in lis:
    print(i)

#to sum up some shit
lis_sum = 0
for i in range(11):
    lis_sum = i + lis_sum
print(lis_sum)

#you can unpack tupples inside a for loop:
    #eaxmple without unpacking:
lis2 = [(1,2,),(3,4,), (5,6,)]
for i in lis2:
    print(i)

for (t1,t2) in lis2:
    print(t1, end=",")
    print(t2)

#iterating through a dictionary
d = {'k1':1,'k2':2,'k3':3}
for item in d:
    print(item) #this produces only the keys. So if you want to have values etc. you'll have to use .items, .values etc.

print(d.items()) #this will print you your dictionary as a list of tupples, which can then by unpacked in for loop. item version thus supports iteration
for (k,v) in d.items():
    print(v, end =" -> ")
    print(k)
#print keys/values as a list. ! as dictionaries are unordered so their order in the list will be arbitrary
print(list(d.keys()))
#but you can sort them now since they're a list
print(list(d.values()))

#########
#While Loops
#########

#exectues the loop as long as condition at beginning is TRUE.
#break: ends the loop if condition is true
#continue: starts the loop all over again (so does not execute whatever is under the continue statement
#pass, does nothing. but if you write a function/Loop but don't have it finished yet you can add it as placeholder and get no error
x = 0
while x <= 10:
    print(x, end= " -> ")
    print(x, "is smaller than 10")
    if x == 9:
        print("I'm breaking because this gets tedious")
        break
    else:
        print("continuing...")
        x+=1

########
#Useful Operators
########

#range: creates a list of integers up to but excluding a cert. value. you can also specify steps. range(start, stop, step)
print(list(range(2,11,2))) #needed the list function because of print function

#enumerate: creates tuples, indexes the content in formula with numbers. you can use this for loops. !index before object in tupple
print(list(enumerate("abcde")))
for (i, letter) in enumerate("abcde"):
    print(f'At index {i} the letter is {letter}')

#zip: creates a list of tupples from two ore more lists
lis1 = list(range(10))
lis2 = ["a","b","c","d","e","f","g","h","i"]
print(len(lis2))
tup = zip(lis1, lis2)
print(list(tup))
for item1,item2 in zip(lis1,lis2):
    print(f'This object "{item1}" is from lis1, this object "{item2}" is from lis2')

#in: to check if an object is in a list. returns true/false
print(2 in lis2)
#you can also do not in
print(2 not in lis2)

#min/max: to find minimum and maximum of a list
print(min(lis1))

#random functions: shuffle, reshuffels an existing list
print(lis1)
from random import shuffle
shuffle(lis1)
print(lis1)

#randit: returns a random integer in a range including edges
from random import randint
print(randint(0,100))

#input: you can then input something in code
#input("Put your name here: ")

#######
#List comprehension
#######

#is basically a for loop in one line, resulting in a list
word = "abcdefg"
lst = [x for x in word]
print(lst) #so for every iteration it creates a list item, based on the specified rules in the loop

lst = [x**2 for x in range(11)]
print(lst)

#with if statements, for example exponential with only odd numbers
lst = [x**2 for x in range(11) if (x%2) !=0]
print(lst)

#you can also work with another list or nest loops
celsius = [0, 13.5, 25, 180]
fahrenheit = [((9/5)*temp + 32) for temp in celsius]
print(fahrenheit)

lst = [x**2 for x in [x**2 for x in range(11)]]
print(lst)

#Test
st = 'Print only the words that start with s in this sentence'
lys = st.split()
print(lys)
for s in st:
    if  s == "s":
        print(s)