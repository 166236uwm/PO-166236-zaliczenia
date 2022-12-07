from pizza import Pizza


class Slice(Pizza):
    how_many_slices: int

    def __init__(self, diameter, toppings, how_many_slices):
        super().__init__(diameter, toppings)
        self.how_many_slices = how_many_slices

        if self.how_many_slices < 4 or self.how_many_slices > 12 or self.how_many_slices % 2 != 0:
            print('błędna ilość kawałków')
            raise ValueError(-10)

    def set_how_many_slices(self, n):
        if n < 4 or n > 12 or n % 2 != 0:
            print('błędna ilość kawałków')
            raise ValueError(-10)
        self._how_many_slices = n

    def get_how_many_slices(self):
        return self._how_many_slices

    how_many_slices = property(get_how_many_slices, set_how_many_slices)

    def part_price(self, ordered_slices):
        return (ordered_slices / self.how_many_slices) * self.price

    def __str__(self):
        s = str(Pizza(self._diameter, self.toppings))
        return s + '\nkawałki ' + str(self.how_many_slices) + '\ncena za kawałek ' + str(self.part_price(1))

