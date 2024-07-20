# The python interpreter has a number of functions and types built into it that are always available

# string build in methods/functions

message = "corona vaccine is ready to use, most of them are more than 90percent effective "
"""
#print(message)
# to print the first letter in capital

print(message.capitalize())

mes = message.capitalize()

print(mes)

# dir() function

print(dir(message))
print()
print(dir([]))
print("xxxxxx")
print(dir(()))
print("xxxxxx")
print(dir({}))



print(message.find("ready"))


seq1 = ("192","168","40","90")

print(".".join(seq1))

print(":".join(seq1))


# adding the data to the list
moutains = ["Everest", "Himalays", "Sahyadri", "Alps", "K2", "Mt Hood"]

moutains.append("Oregon mount")

print(moutains)

# extending the list with my own list

moutains.extend(["Mt Rainer", "Satpura"])

print(moutains)

# if we want to insert at specific position, we can do that using the insert functions and index values

moutains.insert(2, "Mt Abu")
print(moutains)

# to remove the last value in the list -- we use pop

moutains.pop()

print(moutains)

# to remove specific position entry

moutains.pop(5)

print(moutains)
"""
# dictionaries

cntr_emp1 = {"Name":"Santa", "Skill":"Blockchain","Code":1024}

print(cntr_emp1.keys())
print(cntr_emp1.values())
cntr_emp1.clear()

print(cntr_emp1)