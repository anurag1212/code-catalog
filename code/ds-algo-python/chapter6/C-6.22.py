def recursive_postfix(exp, i = None, first = False):
    if i is None:
        i = len(exp)-1
        first = True
    if i<0:
        return 0,i
    if check(exp[i]):
        return int(exp[i]),i
    else:
        re,new_i = recursive_postfix(exp, i-1)
        le,new_new_i = recursive_postfix(exp, new_i-1)
        res = float(do_op(le,exp[i],re))
        return (res, new_new_i) if not first else res

def iterative_postfix(exp):
    i = len(exp)-2
    stack = [exp[-1]]
    while stack:
        # print(stack)
        if len(stack)==1 and check(stack[-1]):
            return stack[-1]
        if stack:
            top = stack.pop()
            if check(top) and check(stack[-1]):
                le = float(top)
                re = float(stack.pop())
                op = stack.pop()
                res = do_op(le, op, re)
                if not stack:
                    return res
                stack.append(res)
                continue
            else:
                stack.append(top)
        stack.append(exp[i])
        i -= 1

def check(string):
    return True if (string[-1] in ([str(i) for i in range(10)])) else False

def do_op(le, op_str, re):
    ops=['+','-','*','/']
    op = ops.index(op_str)
    if op==0:
        res=le+re
    elif op==1:
        res=le-re
    elif op==2:
        res=le*re
    elif op==3:
        res=le/re
    # print(le,ops[op],re,'=',res)
    return str(res)


print(recursive_postfix(
['5', '2', '+', '3', '*', '8', '3', '-', '+', '4', '/']))
print(recursive_postfix(
['1', '3', '4', '3', '*', '44', '4', '/', '4', '*', '-', '-', '*']))
print(iterative_postfix(
['5', '2', '+', '3', '*', '8', '3', '-', '+', '4', '/']))
print(iterative_postfix(
['1', '3', '4', '3', '*', '44', '4', '/', '4', '*', '-', '-', '*']))

# Took me far too long, as well as coding and correcting on the fly
# My first try wasn't right. This wasn't even that hard.
# Leetcode says medium. Good first attempt. Remember, I'm starting from 0.
