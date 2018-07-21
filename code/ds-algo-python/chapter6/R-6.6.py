def bracketmatch(s,i=0,opens="[({",closes="])}"):
    if i>=len(s):
        return True
    if s[i] in closes:
        return i
    if s[i] in opens:
        next = bracketmatch(s,i+1)
        if type(next) is bool:
            return False
        if opens.find(s[i]) == closes.find(s[next]):
            return bracketmatch(s,next+1)
        else:
            return False

print(bracketmatch("(()))"))
