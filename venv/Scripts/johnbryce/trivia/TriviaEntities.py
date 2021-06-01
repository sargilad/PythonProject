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
        for answer in self._answers:
            parsed_answers = parsed_answers + answer + "\n"

        return parsed_answers

    def calc_answer(self, user_answer):
        if self._correctAnswer == user_answer:
            self._score = 1
        else:
            self._score = 0
