# break

for i in "DevOps":
    print (i)
    if i == "O":   # condition
        print(f"found by data that is   {i}")
        break # breaks the loop

print("End of loop")
print("")
print("")
print("")
print("")
print("")

# continue --> skips the loop when the condition is met

for i in "DevOps":
    if i == "O":
        print("Found my data:", i)
        continue
    print(f"Value of i is {i}")

print("End of Loop")