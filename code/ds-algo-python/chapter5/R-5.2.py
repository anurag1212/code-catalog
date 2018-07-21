import sys
data = []
past = 0
for k in range(50):
    a = len(data)
    b = sys.getsizeof(data)
    if b>past:
        print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, b))
    data.append(None)
    past = b
