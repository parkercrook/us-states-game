
class ScoreManager:

    def __init__(self):
        self.score = 0
        self.correct_guesses = []

    def add_point(self, answer):
        self.score += 1
        self.correct_guesses.append(answer)

    def game_won(self):
        if self.correct_guesses == 50:
            return True
        else:
            return False