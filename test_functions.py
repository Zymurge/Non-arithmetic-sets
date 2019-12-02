
import unittest
from mensa.prob30 import find_next
from mensa.prob30 import has_sequence
from mensa.prob30 import run

class TestHasSequence(unittest.TestCase):
    def test_input_min(self):
        """
        Test that it fails on a list shorter than 3 ints
        """
        dataset = [
            ([1, 2], 2, False),
            ([],1, False),
            ([5], 1, False)
        ]
        for case in dataset:
            seq, end, expect = case
            result = has_sequence(seq, end)
            self.assertEqual(result, expect)

    def test_mixed_valid_cases(self):
        """
        Test that it fails on a list shorter than 3 ints
        """
        dataset = [ 
            ([1, 2, 4, 0, 0, 0], 2, False),
            ([5, 6, 7, 0], 2, True),
            ([1, 2, 4, 7, 8, 10, 22, 0, 0], 6, True),
            ([1, 2, 4, 9, 10, 12], 5, False) 
        ]
        for case in dataset:
            seq, end, expect = case
            result = has_sequence(seq, end)
            self.assertEqual(result, expect)

class TestFindNext(unittest.TestCase):
    """ Finds the next valid integer that fits the sequence.
        Starts at position 'pos' from the passed in set and find the next fitting integer under 21.
        Assumes lowest value initial value is 0 and will not exceed 20. Updates 'existing' with the 
        value found and returns that value, or 0 if no valid options found.
    """
    def test_next_number_found(self):
        dataset = [ 
            ([1, 3, 0, 0, 0, 0, 0], 1, [1, 4, 0, 0, 0, 0, 0], 4), 
            ([1, 2, 4, 0, 0, 0, 0], 2, [1, 2, 5, 0, 0, 0, 0], 5), 
            ([1, 3, 0, 0, 0, 0, 0], 2, [1, 3, 4, 0, 0, 0, 0], 4), 
            ([1, 3, 8, 14, 16, 0, 0, 0, 0], 4, [1, 3, 8, 14, 17, 0, 0, 0, 0], 17),
            ([1, 8, 9, 13, 16, 0, 0, 0, 0], 5, [1, 8, 9, 13, 16, 20, 0, 0, 0], 20)   
        ]
        
        for case in dataset:
            exist, pos, update, expect = case # explicit names for clarity
            result = find_next(exist, pos)
            self.assertEqual(result, expect)
            self.assertEqual(exist, update)

    def test_next_number_not_found(self):
        dataset = [ 
            ([1, 2, 20, 0, 0, 0, 0], 2, [1, 2, 0, 0, 0, 0, 0], 0), 
            ([1, 3, 8, 14, 16, 19, 0], 6, [1, 3, 8, 14, 16, 19, 0], 0),
            ([1, 3, 10, 15, 18, 0, 0, 0, 0], 5, [1, 3, 10, 15, 18, 0, 0, 0, 0], 0) 
        ]
        
        for case in dataset:
            exist, pos, update, expect = case # explicit names for clarity
            result = find_next(exist, pos)
            self.assertEqual(result, expect)
            self.assertEqual(exist, update)

class TestRun(unittest.TestCase):
    def test_it(self):
        expected = [1, 2, 6, 7, 9, 14, 15, 18, 20]
        result = run()
        #print("Result: " + str(result))
        self.assertNotEqual(result, 0)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()