class TriviaQuestion:
    question = ""
    question_score: int = 0
    answers = ""
    correctAnswer = ""
    score = 0

    # todo:change to private

    def __init__(self, question, question_score, answers, correct_answer):
        self.question = question
        self.answers = answers
        self.question_score = question_score
        self.correctAnswer = correct_answer

    def get_question(self):
        return self.question

    def get_question_score(self):
        return self.question_score

    def get_available_answers(self):
        return self.answers

    def get_correct_answer(self):
        return self.correctAnswer

    def get_score(self):
        return self.score

    def parse_available_answers(self):
        parsed_answers = ""
        answers = self.answers.split(",")
        for answer in answers:
            parsed_answers = parsed_answers + answer.strip() + "\n"

        return parsed_answers

    def calc_answer(self, user_answer):
        if self.correctAnswer == user_answer:
            self.score = self.question_score


class TriviaQuestions:
    __final_score: int = 0

    def __init__(self):
        self.questions_list = []

    def add_question(self, question):
        self.questions_list.append(question)

    def get_question_by_index(self, q_index):
        return self.questions_list[q_index]

    def get_questions(self):
        return self.questions_list

    def calc_final_score(self) -> str:
        __final_score: int = 0
        for question in self.questions_list:
            __final_score += int(question.get_score())

        return __final_score


class Player:
    __name: str = ""
    __age: str = ""
    __score: str = ""
    __country: str = ""

    def __init__(self, name: str, age: str, country: str):
        self.__name = name
        self.__age = age
        self.__country = country

    def set_score(self, score: str):
        self.__score = score

    def get_score(self):
        return self.__score

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


def get_greeting_by_country(country, name):
    country_dictionary = {"england": "Welcome NAME from COUNTRY. Enjoy the game!",
                          "portugal": "bem-vindo NAME da COUNTRY. Aproveite o jogo"}
    greeting_message = ""

    try:
        greeting_message = country_dictionary[country.lower()]
    except KeyError as e:  # default = english
        greeting_message = country_dictionary["england"]
    finally:
        return greeting_message.replace("NAME", name).replace("COUNTRY", country)
