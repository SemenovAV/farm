from animals.poultry import Poultry


class Hens(Poultry):
    type_animal = 'Кура'

    def __init__(self, name, weight):
        super().__init__(name, weight, 'ко-ко-ко')
