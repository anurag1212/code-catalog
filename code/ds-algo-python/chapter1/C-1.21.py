try:
    stack = []
    while True:
        line = raw_input("Type: ")
        stack.append(line)
except EOFError:
    while stack:
        print(stack.pop())
