def int_log(n,count=0):
    if n==0:
        return count-1
    else:
        return int_log(n//2,count+1)

print(int_log(34))
