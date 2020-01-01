from animals.cow import Cow
from animals.sheep import Sheep

my_barashek = Sheep('Барашек', 100)
my_kudryavyj = Sheep('Кудрявый', 80)
my_manika = Cow('Манька', 400)
print(my_manika.say())
print(my_manika.weight)
print(my_manika.capacity)
print(my_manika.eat(22.7))
print(my_manika.weight)
print(my_manika.capacity)
print(my_manika.eat(22.7))
print(my_manika.weight)
print(my_manika.capacity)

