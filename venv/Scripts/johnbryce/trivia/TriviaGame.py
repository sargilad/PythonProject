from TriviaEntities import *
import configparser
import random

# Collect data from config file
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

# Get random number

random_questions = random.sample(trivia_questions.get_questions(), len(trivia_questions.get_questions()))
for random_question in random_questions:
    print(random_question.get_question())
    print(random_question.parse_available_answers())
    ans = input()
# question1.calc_answer(input())
