def reversestr(s,n=0):
    if n==len(s):
        return ""
    return s[len(s)-n-1]+reversestr(s,n+1)

print(reversestr("pots&pans"))
