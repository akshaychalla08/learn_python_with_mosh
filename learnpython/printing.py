name = "sars_cov_2"
disease = "covid19"

print("The name of the virus is:", name)
print("The name of the virus is {}".format(name))

print("{} is the name of the virus".format(name)) # here advantage is in this method we can place the variable in between the sentence
print("virus is {} and disease name is {}".format(name, disease))
print(name, "is the name of the virus")

# 3rd way - best way

print(f"virus is {name} and disease name is {disease}")

# concatination

print("The virus name is" + " " + name) 