import sys
data = []
past = 0
for k in range(100):
    data.append(k)
for k in range(100):
    a = len(data)
    b = sys.getsizeof(data)
    if past>b:
        print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, b))
    data.pop()
    past = b
