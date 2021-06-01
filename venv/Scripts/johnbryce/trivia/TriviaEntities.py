class TriviaQuestion:

    def __init__(self):
        self._question = ""
        self._answers = ""
        self._correctAnswer = ""
        self._score = ""

    def set_question(self, question):
        self._question = question

    def set_available_answers(self, answers):
        self._answers = answers

    def set_correct_answer(self, answer):
        self._correctAnswer = answer

    def set_score(self, score):
        self._score = score

    def get_question(self):
        return self._question

    def get_available_answers(self):
        return self._answers

    def get_correct_answer(self):
        return self._correctAnswer

    def get_score(self):
        return self._score

    def parse_available_answers(self):
        parsed_answers = ""
        answers = self._answers.split(",")
        for answer in answers:
            parsed_answers = parsed_answers + answer.strip() + "\n"

        return parsed_answers

    def calc_answer(self, user_answer):
        if self._correctAnswer == user_answer:
            self._score = 1
        else:
            self._score = 0


class TriviaQuestions:

    def __init__(self):
        self._questions_list = []

    def add_question(self, question):
        self._questions_list.append(question)

    def get_question_by_index(self, q_index):
        return self._questions_list[q_index]

    def get_questions(self):
        return self._questions_list
    # def calc_final_score(self):
