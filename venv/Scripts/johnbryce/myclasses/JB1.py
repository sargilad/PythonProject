from MySimpleClass import *
from person import *
from vehicle import *
import random

cls = MySimpleClass()
cls._name = "gil"
print(cls.name)
# cls.del_name()
# print(cls.name)

y = InheritClass()
y._name = "ron"
print(y.name)
y.to_override()

# tuple
tpl = 1, 2, 3, 4, 5
print(tpl[1])
print(tpl[::-1])
a, b = tpl[0], tpl[len(tpl) - 1]
b, a = a, b

# Set
ls1 = [1, 2, 3, 4, 5]
ls2 = [4, 5, 6, 7, 8]
sett = {1, 1, 2}
print(set(ls1) | set(ls2))

print("asd")


def pyramid(num: int):
    for i in range(1, num):
        print("*" * i)
    for i in range(num, 0, -1):
        print("*" * i)


pyramid(5)


# Hints in method
def calc(aa: int = 100, bb: int = 200) -> bool:
    return aa == bb


calc1 = calc(aa=200)
print(calc1)


def find_diff(str1: str, str2: str) -> bool:
    if len(set(str1) & set(str2)) == 0:
        return False

    else:
        return True


find_diff("asb", "asd")


def palindrome(my_str: str):
    str_len = len(my_str)
    for i in range(0, str_len):
        if my_str[i] != my_str[str_len - 1 - i]:
            return False
    return True


palindrome("abcba")
palindrome("abccba")


def is_primer(num: int) -> bool:
    for i in range(1, num):
        if i == 1:
            continue
        if num % i == 0:
            return False

    return True


def get_primers_count(num: int) -> int:
    primer_counter = 0
    for i in range(1, num):
        if is_primer(i):
            primer_counter += 1

    return primer_counter


get_primers_count(0)


def analyze_class(students: dict, fail: int = 65, excel: int = 95) -> dict:
    excel_students = []
    fail_students = []
    other_students = []

    for st in students:
        if int(students[st]) <= fail:
            fail_students.append(st)
        elif int(students[st]) >= excel:
            excel_students.append(st)
        else:
            other_students.append(st)

    students_dict = {'excel': excel_students, 'failed': fail_students, 'others': other_students}

    return students_dict


students_lst = {'gil': 100, 'moshe': 40, 'moshe2': 45, 'eli': 66}
s_dict = analyze_class(students_lst, fail=40)
print(s_dict)

# vehicle = __Vehicle()
# vehicle.set_max_speed(1)
bus = Bus()


student = Student("asdasd", "asdasd", 100)
print("asd")
