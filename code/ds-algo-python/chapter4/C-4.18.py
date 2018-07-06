def vovels(s,n=0,v="aeiou"):
    if n==len(s):
        return 0
    if s[n] in v:
        return 1+vovels(s,n+1)
    else:
        return -1+vovels(s,n+1)

def morevovs(s):
    return True if vovels(s)>0 else False

print(morevovs("anuraga"))
