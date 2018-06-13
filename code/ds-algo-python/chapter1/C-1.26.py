def validate():
    a = int(raw_input("First: "))
    b = int(raw_input("Second: "))
    c = int(raw_input("Third: "))

    try:
        return any([bool((eval(str(a)+op+str(b)) == c) or (a == eval(str(b)+op+str(c)))) for op in ["+","-","/","*"]])
    except ZeroDivisionError:
        return "Traded functionality for single-lineness :D"

print(validate())
