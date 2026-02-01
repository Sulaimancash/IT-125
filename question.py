class Question:
    def __init__(self, image_path, text, options, correct_index):
        self.image_path = image_path
        self.text = text
        self.options = options
        self.correct_index = correct_index

    def is_correct(self, answer_index):
        return answer_index == self.correct_index
