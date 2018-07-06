def palin(s,n=0):
    if n>len(s)//2:
        return True
    if s[n] != s[len(s)-1-n]:
        return False
    return True and palin(s,n+1)

print(palin("pots&pans"))
print(palin("abba"))
print(palin("abbba"))
print(palin("b"))
