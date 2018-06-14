class Flower:
    def __init__(self, name="Generic Flower", petals=10, price=0.0):
        if not isinstance(name, str):
            raise ValueError("Provide string for name")
        if not isinstance(petals, int):
            raise ValueError("Provide int for petals")
        if not isinstance(price, float):
            raise ValueError("Provide float for price")

        self._name = name
        self._petals = petals
        self._price = price

    def get_name(self):
        return self._name

    def get_petals(self):
        return self._petals

    def get_price(self):
        return self._price

    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Provide string for name")
        self._name = name

    def set_petals(self):
        if not isinstance(petals, int):
            raise ValueError("Provide int for petals")
        self._petals = petals

    def set_price(self):
        if not isinstance(price, float):
            raise ValueError("Provide float for price")
        self._price = price

    def __str__(self):
        return ("Name: " + str(self._name) +
                "\nPetals: " + str(self._petals) +
                "\nPrice: " + str(self._price))

rose = Flower("Rose", 15, 10.2)
print(rose)

try:
    mogra = Flower("Mogra", 12.3, 10)
except ValueError:
    print("bad value")
