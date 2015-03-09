import unittest
import random
from datetime import date
import site
site.addsitedir('..')
from src.model.ToDo import ToDo

class ToDoTest(unittest.TestCase):
    def test_ordinary(self):
        todo = ToDo('description', '2001-12-25', '2001-12-26', ['tag'])
        self.assertTrue(todo.matches("."))
        self.assertFalse(todo.matches(" "))
        self.assertTrue(todo.matches("g"))
        self.assertTrue(todo.matches("c"))
        self.assertTrue(todo.matches("01"))
        self.assertTrue(todo.matches("6"))
        self.assertFalse(todo.matches("89"))

    def test_boundary(self):
        todo = ToDo('', '2001-12-25', '2001-12-26', [''])
        self.assertTrue(todo.matches("."))
        self.assertFalse(todo.matches(" "))
        self.assertFalse(todo.matches("g"))
        self.assertFalse(todo.matches("c"))
        self.assertTrue(todo.matches("01"))
        self.assertTrue(todo.matches("6"))
        self.assertFalse(todo.matches("89"))

    def test_big(self):
        big_string = "BIG" * 1137
        todo = ToDo(big_string, '2001-12-25', '2001-12-26', [big_string] * 37)
        self.assertTrue(todo.matches("."))
        self.assertFalse(todo.matches(" "))
        self.assertTrue(todo.matches("G"))
        self.assertFalse(todo.matches("C"))
        self.assertTrue(todo.matches("01"))
        self.assertTrue(todo.matches("6"))
        self.assertFalse(todo.matches("89"))

    def test_random_test(self):
        for _ in range(0, 1000):
            rand_day = random.randint(1, 28)
            rand_month = random.randint(1, 12)
            rand_year = random.randint(1970, 2001)
            rand_date = date(rand_year, rand_month, rand_day)

            todo = ToDo('description', str(rand_date), str(rand_date), ['tag'])
            if random.choice([True, False]):
                expected = rand_date
                self.assertEqual(str(rand_date), str(todo.begin_date))
                self.assertEqual(str(rand_date), str(todo.end_date))
            else:
                expected = 0
                self.assertNotEqual(str(expected), str(todo.begin_date))
                self.assertNotEqual(str(expected), str(todo.end_date))

if __name__ == '__main__':
    unittest.main()
