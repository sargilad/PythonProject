class TriviaQuestion:
    question = ""
    answers = ""
    correctAnswer = ""
    score = ""

    def __init__(self, question, answers, correct_answer):
        self.question = question
        self.answers = answers
        self.correctAnswer = correct_answer

    def get_question(self):
        return self.question

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
            self.score = 1
        else:
            self.score = 0


class TriviaQuestions:
    def __init__(self):
        self.questions_list = []

    def add_question(self, question):
        self.questions_list.append(question)

    def get_question_by_index(self, q_index):
        return self.questions_list[q_index]

    def get_questions(self):
        return self.questions_list

    def calc_final_score(self):
        count = 0
        for question in self.questions_list:
            if question.get_score() == 1:
                count += 1

        print(f"you scored {count} out of {len(self.questions_list)}")
