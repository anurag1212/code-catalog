def subsets(pool,used=set(),total=[]):
    if pool:
        used.add(pool.pop())
        total.append(set(used))
        subsets(set(pool),set())
        while(pool):
            used.add(pool.pop())
            total.append(set(used))
    return total

print(subsets(set([x for x in range(10)])))

# THIS TOOK 1.5 HRS wtf
# I gave up on finding a generator version
# and one without using a total
# and one using recursion better
# and im sending new copies
