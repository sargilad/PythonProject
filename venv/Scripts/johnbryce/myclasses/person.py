class Person:
    __first: str
    __last: str

    def __init__(self, first, last):
        self.__first = first
        self.__last = last


class Student(Person):
    __grade: int

    def __init__(self, first, last, grade):
        super().__init__(first, last)
        self.__grade = grade

    def set_grade(self, grade):
        self.__grade = grade
