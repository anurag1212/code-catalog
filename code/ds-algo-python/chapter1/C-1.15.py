def distinct(data):
    return len(data) == len({i for i in data})

print(distinct([2,5,6,8,5]))
print(distinct([2,5,6,8]))
