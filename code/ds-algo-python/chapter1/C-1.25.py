punc = """;"',.?!"""

def removepunc(string):
    return "".join([c for c in string if c not in punc])

print(removepunc("This studyi'ng ses.h is goi.ng goo,d!!?"))
