from animals.dairy import Dairy


class Goats(Dairy):
    type_animal = 'Коза'

    def __init__(self, name, weight):
        super().__init__(name, weight, 'бе-бе-бе')
