import math


class Pizza:

    price: float
    toppings: {str: int}
    diameter: float

    def __init__(self, diameter, toppings):
        self.ilosc_dodatkow = 0
        self.diameter = diameter
        self.toppings = toppings

        if self._diameter < 20:
            print("błędna średnica")
            raise ValueError(-10)
        for x in self.toppings:
            if self.toppings[x] > 3 or self.toppings[x] < 0:
                raise ValueError(-20)
            self.ilosc_dodatkow += self.toppings[x]

        self.price = 0.05 * Pizza.area(self._diameter) + self.ilosc_dodatkow * 2

    @staticmethod
    def area(d):
        return math.pi * (d / 2)

    def set_diameter(self, d: float):
        if d < 20:
            print("błędna średnica")
            raise ValueError(-10)
        self._diameter = d
        self.price = 0.05 * Pizza.area(self._diameter) + self.ilosc_dodatkow * 2

    def add_topping(self, s: str):
        if s in self.toppings:
            self.toppings[s] += 1
        else:
            self.toppings[s] = 1

        self.price += 2

    def __str__(self):
        s = ''
        s += 'Pizza:\nśrednica: ' + str(self._diameter) + '\n'
        dod = ''
        if len(self.toppings) > 0:
            for x in self.toppings:
                dod += x
                if self.toppings[x] > 1:
                    dod += ' x ' + str(self.toppings[x])
                dod += ', '
            dod = dod[:-2]
            s += 'dodatki: '+ dod + '\n'
        s += 'cena: ' + str(self.price) + '\n'
        return s

    def __add__(self, other):
        if self._diameter > other._diameter:
            d = self._diameter
        else:
            d = other._diameter

        temp = Pizza(d, self.toppings)
        for x in other.toppings:
            for y in range(other.toppings[x]):
                temp.add_topping(x)
        return temp

    diameter = property(fset=set_diameter)
