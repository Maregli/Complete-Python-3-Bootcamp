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



