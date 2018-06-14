def init (self, customer, bank, acnt, limit, balance=0):
    """
    Create a new credit card instance.

    The initial balance is zero.

    customer the name of the customer (e.g., John Bowman )
    bank     the name of the bank (e.g., California Savings )
    acnt     the acount identifier (e.g., 5391 0375 9387 5309 )
    limit    credit limit (measured in dollars)
    """
    self._customer = customer
    self._bank = bank
    self._account = acnt
    self._limit = limit
    self._balance = balance
