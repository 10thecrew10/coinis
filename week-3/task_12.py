from typing import List, Dict


class Company:
    def __init__(self, name: str = '', area: str = '', employees: List[Dict] = [], balance: float = 0,
                 max_num_of_employees = 0):
        self._name = name
        self._area = area
        self._employees = employees
        self._balance = balance
        self._max_num_of_employees = max_num_of_employees

    def add_employee(self, e: Dict):
        if len(self.employees) < self.max_num_of_employees:
            self.employees.append(e)

    def can_pay_employees(self):
        return self.balance >= sum(x['salary'] for x in self.employees)

    def __str__(self):
        return f'“name”: “{self.name}”, “area”: “{self.area}”, “balance”:“{self.balance}”'

    def __gt__(self, other):
        return len(self.employees) > len(other.employees)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value

    @property
    def employees(self):
        return self._employees

    @employees.setter
    def employees(self, value):
        self._employees = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value

    @property
    def max_num_of_employees(self):
        return self._max_num_of_employees

    @max_num_of_employees.setter
    def max_num_of_employees(self, value):
        if value >= 0:
            self._max_num_of_employees = value


c1 = Company('ABC', 'IT', [{'name': 'Dino', 'surname': 'Kalac', 'salary': 2000}], 100000, 50)
c2 = Company('Microsoft', 'IT', [], 3000000000, 20000)
print(c1 > c2)
c2.add_employee({'name': 'Una', 'surname': 'Li', 'salary': 2500})
print(c2)