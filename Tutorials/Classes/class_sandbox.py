import random


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        self.temp_pass = first[0] + last[0:3] + str(random.randint(1000, 9999))

    def full_name(
        self,
    ):
        return "{} {}".format(self.first, self.last)


emp_1 = Employee("Tristan", "Payne", 100000)
emp_2 = Employee("Grant", "Bennett", 120000)


print(emp_1.full_name())

print(emp_1.temp_pass)

print(Employee.full_name(emp_2))
