def reverse_list(s,n=None):
    if n is None:
        n = len(s)-1
    if n<len(s)//2:  # Luckily got this right. Should think next time.
        return
    else:
        s[n], s[len(s)-1-n] = s[len(s)-1-n], s[n]
        reverse_list(s,n-1)
        return

s=[1,2,3,4,5]
reverse_list(s)
print(s)
s=[1,2,3,4,5,6]
reverse_list(s)
print(s)
s=[1]
reverse_list(s)
print(s)
s=[1,2]
reverse_list(s)
print(s)
s=[]
reverse_list(s)
print(s)
