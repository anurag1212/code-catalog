def minmax(data):
    min = float('inf')
    max = float('-inf')

    for val in data:
        min = val if min>val else min
        max = val if max<val else max

    return min,max

print(minmax([1,5,7347,-1251]))
