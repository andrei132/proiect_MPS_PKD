import unittest
from src.randomAlgorithm import random_choice, random_numers_between

class TestRandomFunctions(unittest.TestCase):
    def test_random_choice_integer_range(self):
        result = random_choice(1, 5)
        self.assertTrue(1 <= result <= 5)

    def test_random_choice_list(self):
        data_list = ['option1', 'option2', 'option3']
        result = random_choice(data_list)
        self.assertIn(result, data_list)

    def test_random_choice_list_with_number(self):
        data_list = ['option1', 'option2', 'option3']
        result = random_choice(data_list, number=2)
        self.assertEqual(len(result), 2)
        self.assertTrue(all(element in data_list for element in result))

    def test_random_numbers_between(self):
        result = random_numers_between(end=10, count=5)
        self.assertEqual(len(result), 5)
        self.assertTrue(all(0 <= num <= 10 for num in result))

if __name__ == '__main__':
    unittest.main()