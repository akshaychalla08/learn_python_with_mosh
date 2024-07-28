course = 'Python for beginners'
print(len(course))
'''
diff btw functions and methods -- when a function is belongs to the specific to some kind of object like string,
then we ref to that function as a method 
ex : upper() - this function is valid only for strings
whereas -  len, print are general purpose and are referred as funtions
'''
upper = course.upper()
lower = upper.lower()
print(upper)
print(lower)

# to find/locate any data from the string, we use find method(find method is case sensitive)
#Eprint(course.find('64'))

# to replace the string data, we use replace(case sensitive)

#print(course.replace('beginners', 'absolute beginners'))

# to find the sequence of string - we use in method   ----- Case sensitive
# diff btw find and in methods ---> in methods give output in Boolean value, where as find - gives the index of the string

#print('Python' in course)

#course1 = course.title()

#print(course1)

