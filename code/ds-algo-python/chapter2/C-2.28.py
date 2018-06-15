class PredatoryCreditCard(CreditCard):

    def__init__(self, customer, bank, acnt, limit, apr):
        super(). init (customer, bank, acnt, limit)
        self._apr = apr
        self._charges = 0

    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._balance += 5
        else:
            if self._charges >10:
                self._balance += 1
        return success

    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1 + self. apr, 1/12)
            self._balance *= monthly_factor
        self._charges = 0
