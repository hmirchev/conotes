import unittest
import random
import site
site.addsitedir('..')
from src.model.IText import IText

class ITextTest(unittest.TestCase):
    def test_ordinary(self):
        text = IText('description', ['tag'])
        self.assertTrue(text.matches("."))
        self.assertFalse(text.matches(" "))
        self.assertTrue(text.matches("g"))
        self.assertTrue(text.matches("c"))
        self.assertFalse(text.matches("l"))
        self.assertFalse(text.matches("01"))
        self.assertFalse(text.matches("6"))
        self.assertFalse(text.matches("89"))

    def test_boundary(self):
        text = IText('', [''])
        self.assertFalse(text.matches("."))
        self.assertFalse(text.matches(" "))
        self.assertFalse(text.matches("g"))
        self.assertFalse(text.matches("c"))
        self.assertFalse(text.matches("l"))
        self.assertFalse(text.matches("01"))
        self.assertFalse(text.matches("6"))
        self.assertFalse(text.matches("89"))

    def test_big(self):
        big_string = "BIG" * 1137
        text = IText(big_string, [big_string] * 37)
        self.assertTrue(text.matches("."))
        self.assertFalse(text.matches(" "))
        self.assertTrue(text.matches("G"))
        self.assertFalse(text.matches("C"))
        self.assertFalse(text.matches("L"))
        self.assertFalse(text.matches("01"))
        self.assertFalse(text.matches("6"))
        self.assertFalse(text.matches("89"))

    def test_random(self):
        for _ in range(0, 1000):
            rand = random.randint(1, 100)
            text = IText(str(rand), [str(rand)])
            if random.choice([True, False]):
                expected = rand
                self.assertEqual(str(expected), text.description)
            else:
                expected = 0
                self.assertNotEqual(str(expected), text.description)

if __name__ == '__main__':
    unittest.main()
