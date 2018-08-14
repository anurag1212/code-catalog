import random

def rand_weight(tuples):
    sum = sum([w for _,w in tuples])
    r = random.randint(1,sum)
    curr_sum,i = 0
    for _,(ans,w) in tuples:
        curr_sum += w
        if curr_sum>=r: return ans
    return ans

# I remembered this soln sadly. My original thought process was:
# 1) push element i weight_i times to array, but too much space
# 2) Do normal rand, and increment access count of each element,
#    and once it reaches its threshold (determined by its weight)
#    return it, but O(sum(weights)) complexity.
