numbers = [5,2,5,2,2]
'''
value = "x"
for n in numbers:
   for v in value:
      output = n * v
      print(output)
'''

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'L'
    print(output)