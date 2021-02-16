##########
#Functions
##########

# We begin with def then a space followed by the name of the function. Try to keep names relevant, for example len()
# is a good name for a length() function. Also be careful with names, you wouldn't want to call a function the same
# name as a built-in function in Python (such as len).
#
# Next come a pair of parentheses with a number of arguments separated by a comma. These arguments are the inputs for
# your function. You'll be able to use these inputs in your function and reference them. After this you put a colon.
#
# Now here is the important step, you must indent to begin the code inside your function correctly.
# Python makes use of whitespace to organize code. Lots of other programing languages do not do this, so keep that in mind.
#
# Next you'll see the docstring, this is where you write a basic description of the function.
# Using Jupyter and Jupyter Notebooks, you'll be able to read these docstrings by pressing Shift+Tab after a function name.
# Docstrings are not necessary for simple functions, but it's good practice to put them in so you or other people can
# easily understand the code you write.

def say_hello():
    print("hello")
say_hello()

#with arguments:
def greeting(name):
    print(f'hello {name}')
greeting("Thomas")

#testint if github still works after I've moved files