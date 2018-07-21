def recursivepop(S):
    if not S:
        return
    S.pop()
    recursivepop(S)
