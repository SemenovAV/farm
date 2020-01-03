from animals.poultry import Poultry


class Ducks(Poultry):
    type_animal = 'Утка'

    def __init__(self, name, weight):
        super().__init__(name, weight, 'кря-кря')
