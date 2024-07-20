"""
This script will implement our knowledge on conditions and diff data-types
"""

print("This IT organization has various skill sets")
print("Find out your match")

print("Enter Capitalised values")

DevOps = ["Jenkins","Ansible","Bash","Python","Puppet","Dockers","Kubernetes","Terraform"]

Development = ("Nodejs","Angularjs","Java",".net","Python")
cntr_emp1 = {"Name":"Santa", "Skill":"Blockchain","Code":1024}
cntr_emp2 = {"Name":"Rocky","Skill":"AI","Code":1218}

user_skill = input("Enter your desired skill: ")

# print(user_skill)

# check in the db if we have this skill

if user_skill in DevOps :
    print (f"We have {user_skill} in DevOps team.")
elif (user_skill in Development):
    print(f"We have {user_skill} in Development team")
elif (user_skill in cntr_emp1.values()) or (user_skill in cntr_emp2.values()):
    print(f"We have contract employees with {user_skill} skill")
else:
    print("Skill not found") 
    print("please check if you have entered value in capitalize or check the spelling")

