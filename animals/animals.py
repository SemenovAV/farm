class Animals:
    def __init__(self, name, lexicon):
        self.name = name
        self.lexicon = lexicon
        self.satiety = 0

    def eat(self, food):
        if self.satiety < 100:
            self.satiety += food
        elif self.satiety + food > 100:
            self.satiety += food - (self.satiety + food - 100)
            return f'{self.lexicon}-' * 2 + self.lexicon
        return self.satiety

    def say(self):
        return self.lexicon
