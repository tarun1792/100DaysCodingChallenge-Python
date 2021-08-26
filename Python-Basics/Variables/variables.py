# Indentation
## Indentation is important in python
## Unlike other programming languages python uses indentation to idicate a block of code
## The number of spaces is upto the programmer, but it has to be at least one space
## In Same block of code the spacing should be equal otherwise python will through an error
# ----------------------------------------------
# example:
# if 5 > 2:
#  print("something")
#      print("another thing")  <- This is wrong
# -----------------------------------------------
### Because the extra space defies the rule of same indentation for same block of code

print('hello world')

# Python Variable 
a = 100
b = 200
c = a + b
print("Total of a + b = " + str(c)) #If you try to combine a string and a number, Python will give you an error:

# Multiple variable assignements
d,e,f = 100,200,300
print(d)
print(e)
print(f)

# one value to multiple assignment
g = h = i = 400
print(g)
print(h)
print(i)

# Collection UnPack
fruits = ["Mango","Banana","Apple"]
j,k,l = fruits
print(j)
print(k)
print(l)

# Global Variable
m = "Awesome"

def myFunc():
    print("My function is " + m)

myFunc()

# Define a Global Variable inside function

def myfunc():
    global n
    n = "fantastic"

myfunc()
print("my function is "+ n)

# Can change a global variable using global keyword
def MyFunc():
    #global m = "Febulous" -> SyntaxError: invalid synta
    global m
    m = "fabulous"

MyFunc()
print("My Function is " + m)