from employee import Employee
from manager import Manager

p_1 = Employee("Tomasz Bloch", "adres", 2018, {2018: 10.0, 2019: 11.0, 2020: 12.0, 2021: 13.0, 2022: 201.0})
print(p_1)
print(p_1.increase_procent())
p_2 = Employee("Tomasz Bloch", "adres", 2019, {2019: 11.0, 2020: 12.0, 2021: 13.0, 2022: 201.0})
print(p_1 == p_2)
# p_3 = Employee("Tomasz Bloch", "adres", 2022, {2018: 10.0, 2019: 11.0, 2020: 12.0, 2021: 13.0, 2022: 201.0})
# print(p_3)
m_1 = Manager("Tomasz Bloch", "adres", 2018, {2018: 10.0, 2019: 11.0, 2020: 12.0, 2021: 13.0, 2022: 201.0}, 20.0)
print(m_1.is_manager())
