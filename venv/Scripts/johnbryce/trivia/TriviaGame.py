from TriviaEntities import *
import configparser

# q = "What is your name"
# a = ['1.a', '2.b', '3.c', '4.d']
# ca = '1'


config_parser = configparser.ConfigParser()
config_parser.read('questions.ini')
questions_sections_list = config_parser.sections()

trivia_questions = TriviaQuestions()
for question_section in questions_sections_list:
    trivia_question = TriviaQuestion()
    trivia_question.set_question(config_parser.get(question_section, 'question'))
    trivia_question.set_available_answers(config_parser.get(question_section, 'available_answers'))
    trivia_question.set_correct_answer(config_parser.get(question_section, 'correct_answer'))
    trivia_questions.add_question(trivia_question)

trivia_questions.get_question_by_index(0)

print("What is your name?")
# print(question1.parse_available_answers())
# question1.calc_answer(input())
