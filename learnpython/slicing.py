planet1="Closest to  Sun"
print(planet1)

print(planet1[0])
print(planet1[9])

print(planet1[-1]) # -ve starts from the right to left( -1 is n)


# Slicing a string --- get a substring from string

print(planet1[1:5])
print(planet1[:])  # default range(0 : -1)
print(planet1[0:-1]) 
print(planet1[:7])
print(planet1[11:])  

# slicing a tuple

'''
devops = ("Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible")

print(devops[0])
print(devops[4])
print(devops[0:4])
print(devops[0:-1])

print(devops[2:5][0]) # slicing tuple in tuple
print(devops[2:5][0][5:11])  # from the tuple output(string) -slicing that string
print(devops[2:5][0][5:11][2:5]) # slicing string again

print(devops[2:5][0][5:11][2:5][2])   
'''

# slicing a List
'''
devops = ["Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible"]

print(devops[0])
print(devops[4])
print(devops[0:4])
print(devops[0:-1])

print(devops[2:5][0]) # slicing tuple in tuple
print(devops[2:5][0][5:11])  # from the tuple output(string) -slicing that string
print(devops[2:5][0][5:11][2:5]) # slicing string again

print(devops[2:5][0][5:11][2:5][2])  
'''

# Dictionary example

Skills = {"DevOps":("AWS","Jenkins","Python","Ansible"), "Development":["Java","NodeJs",".net"]}

print(Skills)

print(Skills["DevOps"])
print(Skills["Development"])

print(Skills["DevOps"][2][2:5])
