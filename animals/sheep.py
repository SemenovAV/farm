from animals.dairy import Dairy


class Sheep(Dairy):

    def __init__(self, name, weight):
        super().__init__(name, weight, 'бе')
