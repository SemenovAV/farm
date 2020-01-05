class Farmer:
    def __init__(self, farm):
        self.report = []
        self.farm = farm

    def work(self, instructions):
        self.report = []
        for item in instructions:
            for animal in list(filter(lambda elem: type(elem) == item['animal'], self.farm)):
                i = 0
                report = {
                    'type': animal.type_animal,
                    'name': animal.name,
                    'weight': animal.weight,
                    'works': []
                }
                for work in item['works']:
                    i += 1
                    if getattr(animal, work["reason"]):
                        result = getattr(animal, work['work'])()
                    else:
                        result = 0
                    report['works'].append({tuple([work['work'], work['report'], work['unit']]): result})
                self.report.append(report)

    def print_report(self):
        message = 'Отчет о проделанной работе:\n'
        all_report = {}
        for item in self.report:
            message += f'\n{item["type"]} {item["name"]}\nПроделанная работа:\n'
            for work in item['works']:
                for key, value in work.items():
                    if key[2]:
                        old_value = all_report.setdefault(key[1], [0, key[2]])[0]
                        all_report[key[1]][0] = round(old_value + value, 2)
                    if not value:
                        message += f'{key[1]}: не требуется.\n'
                    else:
                        message += f'{key[1]}: {value} {key[2]}\n'
        message += f'\n Всего:\n'
        for key, value in all_report.items():
            message += f'{key}: {value[0]} {value[1]}\n'
        print(message)

    def get_heaviest(self):
        heaviest = ''
        max_weight = 0

        for item in self.farm:
            if item.weight > max_weight:
                max_weight = item.weight
                heaviest = f'{item.type_animal} {item.name}'

        return f'Самый большой вес {max_weight} кг имеет {heaviest}'
