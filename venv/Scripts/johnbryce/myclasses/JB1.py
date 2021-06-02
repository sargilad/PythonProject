from MySimpleClass import *
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
ls1 = [1,2,3,4,5]
ls2 = [4,5,6,7,8]
# print("")
