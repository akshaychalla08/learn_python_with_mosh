import random
import time


Vaccines = ["Moderna", "Pfizer", "Sputnik", "Covaxin","CoronaVac"]

random.shuffle(Vaccines)

print(Vaccines)

Lucky = random.choice(Vaccines)

for vac in Vaccines:
    print(f"******** Testing vaccine {vac} ******")
    time.sleep(2)
    if vac == Lucky:
        print(f" {Lucky} vaccine, Test successful")
        print()
        break
    print("XXXXXXXXX")
    print("Test Failed")
    print("XXXXXXXXXX")
    print()
