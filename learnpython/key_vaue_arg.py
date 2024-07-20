# variable length arguments ** -> key word arguments (must be two *)
# args are stores in the form of tuple
# kwargs in the form of dictionaries

import random
def time_activity(*args, **kwargs):
    '''
    Input: Multiple values for minutes, key=value pair acitivty
    Output: Return sum of minutes + random minute spent on a random acitivity
    '''
 #   print(args)
 #   print(kwargs)
    randoma = random.randint(0,60)
    print(randoma)
    min = sum(args) + randoma
    print(min)
    choice = random.choice(list(kwargs.keys()))
  #  print(choice)
    print(f"A person has to spend {min} minutes for {kwargs[choice]}")

time_activity(10, 20, 10, hobby="Dance", Sport = "Boxing", Fun = "Driving", work = "DEvOps")

