from operator import itemgetter


# --- 1. Классы ---

class Program:
    def __init__(self, id, name, size_mb, comp_id):
        self.id = id
        self.name = name
        self.size_mb = size_mb
        self.comp_id = comp_id


class Computer:
    def __init__(self, id, model):
        self.id = id
        self.model = model


class CompProgram:
    def __init__(self, comp_id, prog_id):
        self.comp_id = comp_id
        self.prog_id = prog_id


# --- 2. Функции-запросы ---

def get_one_to_many(computers, programs):
    return [
        (p.name, p.size_mb, c.model)
        for c in computers
        for p in programs
        if p.comp_id == c.id
    ]


def query_b1(one_to_many):
    """Запрос Б1"""
    return sorted(one_to_many, key=itemgetter(0))


def query_b2(computers, one_to_many):
    """Запрос Б2"""
    result = []
    for c in computers:
        programs_count = len(
            list(filter(lambda x: x[2] == c.model, one_to_many))
        )
        if programs_count > 0:
            result.append((c.model, programs_count))
    return sorted(result, key=itemgetter(1))


def query_b3(computers, programs, comp_programs):
    """Запрос Б3"""
    many_to_many_temp = [
        (c.model, cp.prog_id)
        for c in computers
        for cp in comp_programs
        if c.id == cp.comp_id
    ]

    many_to_many = [
        (p.name, comp_model)
        for comp_model, prog_id in many_to_many_temp
        for p in programs
        if p.id == prog_id
    ]

    result = {}
    for prog_name, comp_model in many_to_many:
        if prog_name.endswith("or"):
            result.setdefault(comp_model, []).append(prog_name)

    return result
