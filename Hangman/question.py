class Question:
    def __init__(self, question, answer, currentGuess, isCorrect):
        self.question = question
        self.answer = answer
        self.currentGuess = currentGuess
        self.isCorrect = isCorrect

    def getQuestion(self):
        return self.question

    def getAnswer(self):
        return self.answer

    def getCurrentGuess(self):
        return self.currentGuess

    def getIsCorrect(self):
        return self.currentGuess
