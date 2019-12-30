from animals.dairy import Dairy


class Cow(Dairy):

    def __init__(self, name, weight):
        super().__init__(name, weight, 'My')
