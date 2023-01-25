class Employee:
    __name: str
    __adress: str
    __year_employment: int
    __salary_increase: dict[int: float]

    def __init__(self, name: str, adress: str, year_employment: int, salary_increase: dict[int: float] = {}):
        self.__name = name
        self.__adress = adress
        self.__year_employment = year_employment
        self.__salary_increase = salary_increase
        if self.first_key() < self.__year_employment:
            print("nieprawidłowa wartość")
            raise ValueError(-10)

    def first_key(self) -> int:
        for x in self.__salary_increase:
            return x

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, x: str) -> None:
        if type(x) is str:
            self.__name = x
        else:
            print("Nieprawidłowa wartość")

    @property
    def adress(self) -> str:
        return self.__adress

    @adress.setter
    def adress(self, x: str) -> None:
        if type(x) is str:
            self.__adress = x
        else:
            print("Nieprawidłowa wartość")

    @property
    def year_employment(self) -> int:
        return self.__year_employment

    @year_employment.setter
    def year_employment(self, x: int) -> None:
        if type(x) is int:
            self.__year_employment = x
        else:
            print("Nieprawidłowa wartość")

    @property
    def salary_increase(self) -> dict[int: float]:
        return self.__salary_increase

    @salary_increase.setter
    def salary_increase(self, s_i: dict[int: float]) -> None:
        if self.first_key() < self.__year_employment:
            print("nieprawidłowa wartość")
        else:
            self.__salary_increase = s_i

    def increase_procent(self) -> float:
        return self.salary_increase[2022] / self.salary_increase[self.year_employment] * 100

    def __str__(self) -> str:
        temp = f'Nazwa pracownika: {self.name}\n' \
               f'Adres: {self.adress}\n' \
               f'Rok zatrudnienia: {self.year_employment}\n' \
               f'Wynagrodzenie w 2022r.: {self.salary_increase[2022]}'
        return temp

    def __eq__(self, other) -> bool:
        if self.name == other.name:
            if self.year_employment == other.year_employment:
                if self.adress == other.adress:
                    return True
        return False
