from myclasses.MySimpleClass import MySimpleClass

cls = MySimpleClass()
cls._name = "gil"
print(cls.name)
cls.del_name()
print(cls.name)


name = input("what is your name")
if name == "gilad":
    print("Correct")
else:
    print("Wrong")
