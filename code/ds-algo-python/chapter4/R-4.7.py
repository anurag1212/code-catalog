def str_to_int(s, n=None):
    if n is None:
        n = len(s)-1
    if n<0:
        return 0
    return int(s[n])*(10**(len(s)-n-1)) + str_to_int(s, n-1)

print(str_to_int("151")*2)
