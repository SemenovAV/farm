from animals.poultry import Poultry


class Geese(Poultry):
    type_animal = 'Гусь'

    def __init__(self, name, weight):
        super().__init__(name, weight, 'га-га-га')
