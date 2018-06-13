# Went ahead with an incompletely thought out approach
# To avoid, think hard of cases where your approach would fail
# BEFORE you start coding
import random

def shufflelist(data):
    done = dict()
    i = 0
    swapped = {i:False for i in range(len(data))}
    while i<len(data):
        index = random.randint(0,len(data)-1)
        if(index in done.values()):
            continue
        else:
            done[i] = index
            i += 1

    print "Done: ", done
    i = 0
    temp = data[i]
    while not all(swapped.values()):
        temp, data[done[i]] = data[done[i]], temp
        swapped[i] = True
        i = done[i]

    return data

print(shufflelist([12,3,1,5,6]))
