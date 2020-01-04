class Farmer:
    def __init__(self, farm):
        self.farm = farm
        self.report = []

    def work(self, instructions):
        for item in instructions:
            for animal in list(filter(lambda elem: type(elem) == item['animal'], self.farm)):
                i = 0
                report = {
                    'type': animal.type_animal,
                    'name': animal.name,
                    'weight': animal.weight,
                    'works': {}
                }
                for work in item['works']:
                    i += 1
                    if getattr(animal, work["reason"]):
                        result = getattr(animal, work['work'])()
                    else:
                        result = 'Нет надобности.'
                    report['works'][work['work']] = result
                self.report.append(report)
        self.print_report()

    def print_report(self):
        print(self.report)
