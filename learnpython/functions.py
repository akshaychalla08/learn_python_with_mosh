"""
def add(arg1, arg2):
    total = arg1 + arg2
    return total

# if return is not mentioned, it will return by default null

out = add(1,4)

print(out)

# OR
print(add(2,6))

"""
# ------------------

"""
def add(arg1, arg2):
    total = arg1 + arg2
    
print(add(5,8))   # this returns null value



# ------------------
def add(arg1, arg2):
    total = arg1 + arg2
    print(total)
    return total  # if return is not mentioned in the code block, by default return will be added with none value. "return none"
#print(add(10,50))

(add(10,50))
print(add(10,50))  # this again returns null value -- as None




#### -----------------------

def summ(arg):
    x = 0
    for i in arg:
        x = x + i
    return x

# out = summ([10, 20, 40])

# print(out)
summ([10,'12'])

"""

# default arguements

def greetings(MSG="Morning"):
    print(f"Good {MSG}")
    print("Welcome to the function,")

print(greetings())
greetings("Evening")