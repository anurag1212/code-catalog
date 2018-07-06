def nth_harmonic(n):
    if n==1:
        return 1
    else:
        return 1/n+nth_harmonic(n-1)

print(nth_harmonic(998))
