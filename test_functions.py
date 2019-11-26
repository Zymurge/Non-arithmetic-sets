
import unittest
from mensa.prob30 import find_next
from mensa.prob30 import has_sequence
from mensa.prob30 import run


class TestHasSequence(unittest.TestCase):
    def test_input_min(self):
        """
        Test that it fails on a list shorter than 3 ints
        """
        dataset = [ [1, 2],[],[5] ]
        for case in dataset:
            result = has_sequence(case)
            self.assertEqual(result, False)

    def test_mixed_valid_cases(self):
        """
        Test that it fails on a list shorter than 3 ints
        """
        dataset = [ ([1, 2, 4],False), ([5, 6, 7],True), ([1, 2, 4, 7, 8, 10, 22],True), ([1, 2, 4, 9, 10, 12],False) ]
        for case in dataset:
            result = has_sequence(case[0])
            self.assertEqual(result, case[1])

class TestFindNext(unittest.TestCase):
    def test_next_number_found(self):
        dataset = [ ([1, 2, 4], 5, 5), ([1, 2, 4], 6, 8), ([1, 3, 9, 14, 16], 18, 20) ]
        for case in dataset:
            result = find_next(case[0], case[1])
            self.assertEqual(result, case[2])

    def test_next_number_none(self):
        dataset = [ ([1, 2, 4, 7, 8, 10], 11, 0), ([12, 14, 15, 17], 18, 0) ]
        for case in dataset:
            result = find_next(case[0], case[1])
            self.assertEqual(result, case[2])

class TestRun(unittest.TestCase):
    def test_it(self):
        expected = [1, 2, 6, 7, 9, 14, 15, 18, 20]
        result = run()
        #print("Result: " + str(result))
        self.assertNotEqual(result, 0)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()