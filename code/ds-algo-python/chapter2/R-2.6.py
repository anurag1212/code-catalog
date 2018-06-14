def charge(self, price):
    if not isinstance(price, int):
        raise ValueError("Enter int")
    if price + self. balance > self. limit:
        return False
    else:
        self. balance += price
        return True

def make_payment(self, amount):
    if not isinstance(price, int):
        raise ValueError("Enter int")
    elif price < 0:
        raise ValueError("Enter positive int")
    self. balance −= amount
