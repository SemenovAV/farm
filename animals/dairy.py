from animals.animals import Animals


class Dairy(Animals):

    def __init__(self, name, lexicon, weight):
        super().__init__(name, lexicon, weight)
        self.milk = self.saturation / 2

    def give_milk(self):
        milk = self.milk
        self.milk = 0
        self.saturation -= self.saturation / 2
        return milk

    def eat(self, food):
        result = super().eat(food)
        self.milk += self.saturation / 2
        return result
