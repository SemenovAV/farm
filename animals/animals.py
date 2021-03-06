class Animals:
    def __init__(self, name, weight, lexicon):
        self.name = name
        self.lexicon = lexicon
        self.saturation = 0
        self.hunger = True
        self.weight = weight
        self.capacity = round(weight / 22, 2)

    def eat(self, food=False):
        if not food:
            food = self.capacity
        self.weight += round(food / 100, 2)
        self.capacity = round(self.weight / 22, 2)
        if self.saturation + food > self.capacity:
            surplus = food - (self.capacity - self.saturation)
            self.saturation += (food - surplus)
            return surplus
        self.saturation += food
        self.hunger = self.saturation == self.capacity
        return self.saturation

    def say(self):
        return self.lexicon

    def weigh_myself(self):
        return self.weight
