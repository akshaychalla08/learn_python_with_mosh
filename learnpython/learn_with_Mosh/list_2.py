# list methods/ list functions

numbers = [5,2,1,4,7,5,10]
#numbers.append(34)  - > to add the item to the list,(this adds to the end)
#numbers.insert(4, 'akshay') # if want to insert the data, at particular index

#numbers.clear()

# numbers.pop()
# numbers.remove(7) # removes the first occurance of the value
# numbers.sort()   # to sort the values in ascending
# numbers.reverse() # to reverse the order

# print(numbers.index(10)) # if the value is not in the list, throws the error, other way is to use 'in' - this gives boolean value

# print(1 in numbers )

print(numbers.count(5)) # to check the occurence of the value

"""
for n in numbers:
    if numbers.count(n) > 0:
        numbers.remove(n)

print(numbers)

Tried - but failed
"""
num = [5,2,1,4,7,5,10, 4, 3, 5,10]

unique = []

for n in num:
    if n not in unique:
        unique.append(n)

print(unique)


# unpacking

coordinates = (2,3,4)
'''
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
'''
# instead of writing like above, we can use function called unpacking
# this unpacking, can be used for both list and tuples

x,y,z = coordinates
print(y)
print(x)



