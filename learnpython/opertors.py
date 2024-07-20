# comparison operators
'''
a = 30
b =45

out = (a < b)
print(out)

out = (a == b)
print(out)

out = (a != b)      # not equal to !=
print(out)

# assignment operators

c = 0
d = 1

c+=d  # c = c + d


c-=d
print(c)

# logical operators --  and , or


a = 3
b = 5
x =7
y = 6

out = (a<b) or (x < y)
print(out)

out = (a>b) or (x > y)
print(out)

out = (a>b) and (x > y)

print(out)

out = not(a>b)
print(out)

'''
# membership operators  - in, not in

devops = ["Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible"]

ans  = "Linux" not in devops
ans1  = "Linux"  in devops

print(ans)
print(ans1)

# identity operators

e =5
f =6
result = e is f
result1 = e is not f
print(result)
print(result1)
