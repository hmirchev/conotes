import unittest
import random
import site
site.addsitedir('..')
from src.model.Note import Note

class NoteTest(unittest.TestCase):
    def test_ordinary(self):
        note  = Note('title', 'description', ['tag'])
        self.assertTrue(note.matches("."))
        self.assertFalse(note.matches(" "))
        self.assertTrue(note.matches("g"))
        self.assertTrue(note.matches("c"))
        self.assertTrue(note.matches("l"))
        self.assertFalse(note.matches("01"))
        self.assertFalse(note.matches("6"))
        self.assertFalse(note.matches("89"))

    def test_boundary(self):
        note = Note('', '', [''])
        self.assertFalse(note.matches("."))
        self.assertFalse(note.matches(" "))
        self.assertFalse(note.matches("g"))
        self.assertFalse(note.matches("c"))
        self.assertFalse(note.matches("l"))
        self.assertFalse(note.matches("01"))
        self.assertFalse(note.matches("6"))
        self.assertFalse(note.matches("89"))

    def test_big(self):
        big_string = "BIG" * 1137
        note = Note(big_string, big_string, [big_string] * 37)
        self.assertTrue(note.matches("."))
        self.assertFalse(note.matches(" "))
        self.assertTrue(note.matches("G"))
        self.assertFalse(note.matches("C"))
        self.assertFalse(note.matches("L"))
        self.assertFalse(note.matches("01"))
        self.assertFalse(note.matches("6"))
        self.assertFalse(note.matches("89"))

    def test_random(self):
        for _ in range(0, 1000):
            rand = random.randint(1, 100)
            note = Note(str(rand), str(rand), [str(rand)])
            if random.choice([True, False]):
                expected = rand
                self.assertEqual(str(expected), note.description)
                self.assertEqual(str(expected), note.title)
            else:
                expected = 0
                self.assertNotEqual(str(expected), note.description)
                self.assertNotEqual(str(expected), note.title)

if __name__ == '__main__':
    unittest.main()
