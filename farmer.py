class Farmer:
    def __init__(self, farm):
        self.farm = farm
        self.report = ''

    def work(self, instructions):
        for item in instructions:
            animals = list(filter(lambda elem: type(elem) == item['animal'], self.farm))
            for animal in animals:
                i = 0
                self.report += f'{animal.type_animal} {animal.name}:\n'
                for work in item['works']:
                    i += 1
                    if getattr(animal, work["reason"]):
                        result = getattr(animal, work['work'])()
                    else:
                        result = 'Нет надобности.'
                    self.report += f'{i}. {work["report"]}: {result} {work["unit"]}\n'
        self.print_report()

    def print_report(self):
        print(self.report)
