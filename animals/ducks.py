from animals.poultry import Poultry


class Ducks(Poultry):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'кря')
