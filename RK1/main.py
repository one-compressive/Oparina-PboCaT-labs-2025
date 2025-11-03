from operator import itemgetter

# --- 1. Определение классов данных ---

class Program:
    """Программа (сторона 'много')"""
    def __init__(self, id, name, size_mb, comp_id):
        self.id = id
        self.name = name
        self.size_mb = size_mb  # Количественный признак
        self.comp_id = comp_id  # FK для 1:M

class Computer:
    """Компьютер (сторона 'один')"""
    def __init__(self, id, model):
        self.id = id
        self.model = model

class CompProgram:
    """Программы Компьютера (для M:M)"""
    def __init__(self, comp_id, prog_id):
        self.comp_id = comp_id
        self.prog_id = prog_id

# --- 2. Тестовые данные ---

computers = [
    Computer(1, 'Office PC 1'),
    Computer(2, 'Gaming Rig X'),
    Computer(3, 'Laptop Pro'),
    Computer(11, 'Server Rack A'),
    Computer(22, 'Old Desktop'),
]

programs = [
    Program(1, 'Word Processor', 150, 1),
    Program(2, 'Video Editor', 5000, 2),
    Program(3, 'Spreadsheet App', 200, 3),
    Program(4, 'Antivirus Suite', 300, 3),
    Program(5, 'Image Viewer', 50, 3),
]

comp_programs = [
    CompProgram(1, 1),
    CompProgram(1, 2),
    CompProgram(2, 2),
    CompProgram(2, 3),
    CompProgram(2, 4),
    CompProgram(3, 1),
    CompProgram(3, 4),
    CompProgram(3, 5),
    CompProgram(11, 1),
    CompProgram(22, 2),
]

# --- 3. Разработка запросов (Вариант Б) ---

def main():
    """Основная функция"""

    one_to_many = [
        (p.name, p.size_mb, c.model)
        for c in computers
        for p in programs
        if p.comp_id == c.id
    ]

    many_to_many_temp = [
        (c.model, cp.comp_id, cp.prog_id)
        for c in computers
        for cp in comp_programs
        if c.id == cp.comp_id
    ]

    many_to_many = [
        (p.name, p.size_mb, comp_model)
        for comp_model, comp_id, prog_id in many_to_many_temp
        for p in programs if p.id == prog_id
    ]

    print('Запрос Б1: Список связанных Программ и Компьютеров, отсортированный по Программам ***')
    # Сортировка по Названию программы (индекс 0)
    res_b1 = sorted(one_to_many, key=itemgetter(0))
    print(res_b1, '\n')

    print('Запрос Б2: Список Компьютеров с количеством Программ, отсортированный по количеству Программ ***')
    res_b2_unsorted = []
    for c in computers:
        # Список программ на данном компьютере
        c_programs = list(filter(lambda i: i[2] == c.model, one_to_many))

        if len(c_programs) > 0:
             # Модель и количество программ
            res_b2_unsorted.append((c.model, len(c_programs)))

    # Сортировка по количеству программ (индекс 1)
    res_b2 = sorted(res_b2_unsorted, key=itemgetter(1))
    print(res_b2, '\n')

    print('Запрос Б3: Список Программ, у которых название заканчивается на «or», и модели их Компьютеров (из M:M) ***')
    res_b3 = {}

    # Фильтр: название программы заканчивается на 'or'
    filtered_programs = list(filter(lambda x: x[0].endswith('or'), many_to_many))

    for prog_name, _, comp_model in filtered_programs:
        if comp_model not in res_b3:
            res_b3[comp_model] = []
        if prog_name not in res_b3[comp_model]:
            res_b3[comp_model].append(prog_name)

    print(res_b3)

if __name__ == '__main__':
    main()
