from animals.animals import Animals


class Sheep(Animals):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'ме')
        self.wool = 2000

    def give_wool(self):
        result = self.wool
        self.wool = 0
        self.saturation = 0
        return result

    def eat(self, food):
        result = super().eat(food)
        self.wool += round((self.saturation / 180), 0)
        return result
