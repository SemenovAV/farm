class Animals:
    def __init__(self, name, lexicon, weight):
        self.name = name
        self.lexicon = lexicon
        self.saturation = 0
        self.weight = weight
        self.capacity = round(weight / 22, 2)

    def eat(self, food):
        self.weight += food / 100
        if self.saturation + food >= self.capacity:
            surplus = food - (self.capacity - self.saturation)
            self.saturation += (food - surplus)
            return surplus
        self.saturation += food
        return f'{self.lexicon}-' * 2 + self.lexicon

    def say(self):
        return self.lexicon
