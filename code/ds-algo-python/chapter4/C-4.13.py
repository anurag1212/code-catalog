def product(m,n):
    if n==0:
        return 0
    else:
        return m+product(m,n-1)

print(product(5,16))
