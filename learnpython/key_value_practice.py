import random

def time_activity(*arg1, **kwarg):
    min = sum(arg1) + random.randint(1,5)
    choice = random.choice(list(kwarg.keys()))
    print(f"A person has to spend {min} minutes for {kwarg[choice]}")

time_activity(10, 20, 10, hobby="Dance", Sport = "Boxing", Fun = "Driving", work = "DEvOps")
