from question import Question

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.current = 0
        self.correct = 0
        self.wrong = 0

    def get_current_question(self):
        if self.current < len(self.questions):
            return self.questions[self.current]
        return None

    def answer(self, index):
        q = self.get_current_question()
        if q and q.is_correct(index):
            self.correct += 1
        else:
            self.wrong += 1
        self.current += 1
        return self.get_current_question()
