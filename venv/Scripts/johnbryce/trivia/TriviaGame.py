from TriviaEntities import TriviaQuestion

q = "What is your name"
a = ['1.a', '2.b', '3.c', '4.d']
ca = '1'

question1 = TriviaQuestion()
question1.set_question(q)
question1.set_available_answers(a)
question1.set_correct_answer(ca)
print("What is your name?")
print(question1.parse_available_answers())
# question1.calc_answer(input())
