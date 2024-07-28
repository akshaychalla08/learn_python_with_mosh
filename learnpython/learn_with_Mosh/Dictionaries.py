customers = {
    "name" : "Akshay",
    "Age" : 28,
    "gender":"Male"
}

# print(customers["name"])
# if the key is not avaialable in the dictionary, the output throws error
# to avoid, we can use get - this will give 'none' ,if the key is not there


print(customers.get("Age"))

customers["birthplace"] = "Sindhanur"
# if the key is not there in the dict, we can supply default value like below

customers["name"] = "Kumar"
print(customers.get("birthplace"))

print(customers.get("Birthplace", "Jawalgera"))
print(customers["name"])

