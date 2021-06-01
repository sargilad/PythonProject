from myclasses.MySimpleClass import *
import random

from myclasses.TriviaClass import MyTriviaClass

cls = MySimpleClass()
cls._name = "gil"
print(cls.name)
# cls.del_name()
# print(cls.name)

y = InheritClass()
y._name = "ron"
print(y.name)
y.to_override()

# name = input("what is your name")
# if name == "gilad":
#     print("Correct")
# else:
#     print("Wrong")


# Trivia
q = "What is your name"
a = ['1.a', '2.b', '3.c', '4.d']
ca = '1'

question1 = MyTriviaClass()
question1.set_question(q)
question1.set_available_answers(a)
question1.set_correct_answer(ca)
print("What is your name?")
print(question1.parse_available_answers())
# question1.calc_answer(input())

random.sample(range(3), 3)



