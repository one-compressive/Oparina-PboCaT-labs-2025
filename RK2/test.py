import unittest
from main import (
    Computer,
    Program,
    CompProgram,
    get_one_to_many,
    query_b1,
    query_b2,
    query_b3
)



class TestRK2(unittest.TestCase):

    def setUp(self):
        self.computers = [
            Computer(1, 'Office PC 1'),
            Computer(2, 'Gaming Rig X'),
            Computer(3, 'Laptop Pro'),
        ]

        self.programs = [
            Program(1, 'Word Processor', 150, 1),
            Program(2, 'Video Editor', 5000, 2),
            Program(3, 'Spreadsheet App', 200, 3),
        ]

        self.comp_programs = [
            CompProgram(1, 1),
            CompProgram(2, 2),
            CompProgram(3, 1),
            CompProgram(3, 2),
        ]

        self.one_to_many = get_one_to_many(self.computers, self.programs)

    def test_query_b1_sorting(self):
        """Тест запроса Б1: сортировка по названию программы"""
        result = query_b1(self.one_to_many)
        self.assertEqual(result[0][0], 'Spreadsheet App')

    def test_query_b2_count(self):
        """Тест запроса Б2: количество программ"""
        result = query_b2(self.computers, self.one_to_many)
        self.assertIn(('Laptop Pro', 1), result)

    def test_query_b3_filter(self):
        """Тест запроса Б3: фильтр по окончанию 'or'"""
        result = query_b3(self.computers, self.programs, self.comp_programs)
        self.assertIn('Office PC 1', result)
        self.assertIn('Word Processor', result['Office PC 1'])


if __name__ == '__main__':
    unittest.main()
