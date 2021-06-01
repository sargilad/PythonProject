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






