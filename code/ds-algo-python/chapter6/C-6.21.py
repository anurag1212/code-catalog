def subets_of_set(s):
    stk = []
    i=0
    max = 0
    count = 0
    for a in s:
        stk.append(([a], i))
        i+=1
    while stk:
        max = max if max > stk.__sizeof__() else stk.__sizeof__()
        curr = stk.pop()
        count +=1
        print(curr[0])
        if curr[-1] != len(s)-1:
            for i in range(curr[-1]+1,len(s)):
                curr[0].append(s[i])
                stk.append((list(curr[0]),i))
                curr[0].pop()
    print(max, count)

subets_of_set([a for a in range(6)])

# Took 45 minutes. The first ~30 minutes were useless.
# Did my usual thing of thinking how do i do this instead
# of actually thinking about how to do it. Then the half-
# hearted tries in my head. This time i moved to paper
# quickly enough, good. Then the half hearted tried on paper
# getting a sorta kinda solution's vague idea in my head
# and immediately trying to code thinking i'd got it.
# During the last 15 minutes, i listed down an example
# exhaustively, and actually solidified the idea i had before,
# and coding took barely 5 minutes.
