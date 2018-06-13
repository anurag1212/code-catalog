vovels = {'a', 'e', 'i', 'o', 'u'}

def countvovels(string):
    return sum([1 for c in string if c.lower() in vovels])

print(countvovels("anurAg"))
