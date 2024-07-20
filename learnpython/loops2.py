Vaccines = ["Moderna", "Pfizer", "Sputnik", "Covaxin"]
# nested loops
"""
for vac in Vaccines:
    print(" ")
    print("I would like to take a shot of ")
    for v in vac:
      print(v)  

"""
import time
x = 2

while True:
    print("The value of x is", x)
    print("looping")
    x*=2
    time.sleep(0.001)

