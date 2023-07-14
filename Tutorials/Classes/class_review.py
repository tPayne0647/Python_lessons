class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []
        self.attendance = {}

    def add_grade(self, grade):
        if isinstance(grade, Grade):
            self.grades.append(grade)

    def get_average(self):
        total_grades = 0
        num_grades = len(self.grades)

        if num_grades == 0:
            return 0

        for grade in self.grades:
            total_grades += grade.score
        average = total_grades / num_grades
        return average

    def get_attendance(self, date):
        if date in self.attendance:
            if self.attendance[date]:
                return "{n} was present on {d}".format(n=self.name, d=date)
            else:
                return "{n} was not present on {d}".format(n=self.name, d=date)
        else:
            return "{n}'s attendance on {d} is not recorded.".format(n=self.name, d=date)


class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score

    def is_passing(self):
        if self.score >= Grade.minimum_passing:
            return "Passing Score"
        else:
            return "Does not meet minimum requirements."


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

# Testing
pieter.add_grade(Grade(100))
pieter.add_grade(Grade(64.5))
pieter.add_grade(Grade(76))
pieter_grade_average = pieter.get_average()
print("Pieters average grade is : {}".format(pieter_grade_average))

pieter.attendance = {"7/7": True}
pieter.attendance["7/4"] = False
print(pieter.get_attendance("7/7"))
print(pieter.get_attendance("7/4"))
print(sandro.get_attendance("7/4"))
