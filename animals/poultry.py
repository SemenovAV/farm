from animals.animals import Animals


class Poultry(Animals):

    def __init__(self, name, weight, lexicon):
        super().__init__(name, weight, lexicon)
        self.eggs = round((self.saturation / 90), 0)

    def lay_eggs(self):
        return self.eggs
