from animals.animals import Animals


class Dairy(Animals):

    def __init__(self, name,  weight, lexicon):
        super().__init__(name, weight, lexicon)
        self.milk = self.saturation / 2

    def give_milk(self):
        milk = self.milk
        self.milk = 0
        self.saturation = 0
        return milk

    def eat(self, food=False):
        result = super().eat(food)
        self.milk += self.saturation / 2
        return result
