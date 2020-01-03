from animals.cow import Cow
from animals.goats import Goats
from animals.hens import Hens
from animals.ducks import Ducks
from animals.sheep import Sheep

my_roga = Goats('Рога', 100)
my_kopyta = Goats('Копыта', 80)
my_manika = Cow('Манька', 400)
my_koko = Hens('Ко-ко', 2)
my_kukareku = Hens('Кукареку', 1)
my_kriakva = Ducks('Кряква', 2)
my_barashek = Sheep('Барашек', 100)
my_kudriavyi = Sheep('Кудрявый', 100)

print(my_kukareku.say())
print(my_kukareku.weight)
print(my_kukareku.capacity)
print(my_kukareku.eat(22.7))
print(my_kukareku.weight)
print(my_kukareku.capacity)
print(my_kukareku.eat(22.7))
print(my_kukareku.weight)
print(my_kukareku.capacity)

