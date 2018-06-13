import random

def mychoice(data):
    return data[random.randrange(0,len(data))]

print(mychoice([1,552,123,9512,6344,-1251]))
