from employee import Employee


class Manager(Employee):
    __promotion_threshold: float

    def __init__(self, name: str, adress: str, year_employment: int, salary_increase: dict[int: float], promotion_threshold: float = 10):
        if promotion_threshold < 10:
            print("nieprawidłowa wartość")
            raise ValueError(-10)
        self.__promotion_threshold = promotion_threshold
        super().__init__(name, adress, year_employment, salary_increase)

    @property
    def promotion_threshold(self) -> float:
        return self.__promotion_threshold

    @promotion_threshold.setter
    def promotion_threshold(self, x: float) -> None:
        if x < 10:
            print("nieprawidłowa wartość")
        self.__promotion_threshold = x

    def is_manager(self) -> bool:
        if self.increase_procent() > self.promotion_threshold:
            return True
        return False
