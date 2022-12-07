from pizza import Pizza
from slice import Slice


def main():
    # testy do pizzy

    p_1 = Pizza(23, {'ser': 2, 'szynka': 1})
    p_2 = Pizza(29, {'pieczary': 2, 'oliwki': 1})
    print(p_1, p_2)
    p_1.diameter = 35
    p_1.add_topping('oliwki')
    print(p_1)
    p_1.add_topping('oliwki')
    print(p_1.price)
    print(p_1 + p_2)

    # testy do kawałka

    s_1 = Slice(23, {'ser': 2, 'szynka': 1}, 10)
    print(s_1)
    print(s_1.part_price(5))

main()