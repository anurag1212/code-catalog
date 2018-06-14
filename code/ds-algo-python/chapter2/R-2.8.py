for val in range(1, 17):
    wallet[0].charge(val)
    wallet[1].charge(2*val)
    wallet[2].charge(3*val)

"""
Man this is just math
sum(range(1,...))
"""
