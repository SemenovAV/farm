from animals.cow import Cow
from animals.goats import Goats
from animals.hens import Hens
from animals.ducks import Ducks
from animals.sheep import Sheep
from farmer import Farmer

my_roga = Goats('Рога', 102)
my_kopyta = Goats('Копыта', 89)
my_manika = Cow('Манька', 398)
my_koko = Hens('Ко-ко', 2)
my_kukareku = Hens('Кукареку', 1)
my_kriakva = Ducks('Кряква', 2)
my_barashek = Sheep('Барашек', 106)
my_kudriavyi = Sheep('Кудрявый', 100)

my_farm = {my_roga, my_barashek, my_koko, my_kopyta, my_kriakva, my_kudriavyi, my_kukareku, my_manika}

all_animals_work = [
    {
        'work': 'say',
        'report': 'голос проверил',
        'reason': 'lexicon',
        'unit': ''
    },
    {
        'work': 'eat',
        'report': 'дал корма',
        'reason': 'hunger',
        'unit': 'кг'
    },
    {
        'work': 'weigh_myself',
        'report': 'вес',
        'reason': 'weight',
        'unit': 'кг'
    }
]
dairy_works = [
    {
        'work': 'give_milk',
        'report': 'надоил молока',
        'reason': 'milk',
        'unit': 'л'
    }
]
poultry_works = [
    {
        'work': 'lay_eggs',
        'report': 'собрал яйца',
        'reason': 'eggs',
        'unit': 'шт'
    }
]
sheep_works = [
    {
        'work': 'give_wool',
        'report': 'настриг шерсти',
        'reason': 'wool',
        'unit': 'кг'
    }
]

instructions = [
    {
        'animal': Goats,
        'works': all_animals_work + dairy_works

    },
    {
        'animal': Cow,
        'works': all_animals_work + dairy_works
    },
    {
        'animal': Sheep,
        'works': all_animals_work + sheep_works

    },
    {
        'animal': Hens,
        'works': all_animals_work + poultry_works
    },
    {
        'animal': Ducks,
        'works': all_animals_work + poultry_works
    }
]

my_farmer = Farmer(my_farm)

my_farmer.work(instructions)
my_farmer.print_report()
print(my_farmer.get_heaviest())