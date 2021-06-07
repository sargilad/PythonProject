from TriviaEntities import *
from csvfactory import HighScoreManager
import configparser
import random

# Constants
CORRECT_ANSWER = 'correct_answer'
AVAILABLE_ANSWERS = 'available_answers'
QUESTION = 'question'
QUESTION_SCORE = 'question_score'


def main():
    # read high score
    # manager = HighScoreManager("high_score.csv")

    # data = [{'name': 'moshe', 'score': 50},{'name': 'david', 'score': 70}]
    # manager.write_file(data)

    # dict = manager.read_file()


    # manager.is_new_high_score(30)

    # data1 = {'name': 'simon', 'score': 80}
    # manager.append_file(data1)

    # manager.add_high_score_to_file(data1)


    # Collect data from config file
    config_parser = configparser.ConfigParser()
    config_parser.read('questions.ini')
    questions_sections_list = config_parser.sections()

    trivia_questions = TriviaQuestions()
    for question_section in questions_sections_list:
        trivia_question = TriviaQuestion(question=config_parser.get(question_section, QUESTION),
                                         answers=config_parser.get(question_section, AVAILABLE_ANSWERS),
                                         question_score=config_parser.get(question_section, QUESTION_SCORE),
                                         correct_answer=config_parser.get(question_section, CORRECT_ANSWER))
        trivia_questions.add_question(trivia_question)

    name = input("What is your name?\n")
    age = input("What is your age?\n")
    country = input("What is your country?\n")

    if int(age) < 16:
        print("You are under aged. Game aborted")
    else:
        player = Player(name, age, country)
        greeting_msg = get_greeting_by_country(country, name)

        print(greeting_msg)

        # Get random question
        random_questions = random.sample(trivia_questions.get_questions(), len(trivia_questions.get_questions()))
        for random_question in random_questions:
            print(random_question.get_question())
            print(random_question.parse_available_answers())
            random_question.calc_answer(input())

        # calculate final result
        score = trivia_questions.calc_final_score()
        player.set_score(score)
        print(f"{player.get_name()} - your score is {player.get_score()}")


if __name__ == "__main__":
    main()
