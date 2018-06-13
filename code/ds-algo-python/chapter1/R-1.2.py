def is_even(k):
    if str(k)[-1] in [str(x) for x in range(0,9,2)]:
        return True
    return False

print(is_even(5))
print(is_even(44))
print(is_even(-1512))
print(is_even(-513.5))
print(is_even("anurag"))
