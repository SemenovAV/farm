from animals.dairy import Dairy


class Cow(Dairy):
    type_animal = 'Корова'

    def __init__(self, name, weight):
        super().__init__(name, weight, 'мy-му-му')
