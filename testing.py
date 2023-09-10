import unittest
from QuestionEight import move_direction

class TestMoveDirection(unittest.TestCase):

    def test_invalid_position(self):
        with self.assertRaises(ValueError) as context:
            move_direction("N", 8, 5)
        self.assertEqual(str(context.exception), "Invalid position")

        with self.assertRaises(ValueError) as context:
            move_direction("S", 6, 8)
        self.assertEqual(str(context.exception), "Invalid position")

        with self.assertRaises(ValueError) as context:
            move_direction("N", -1, 5)
        self.assertEqual(str(context.exception), "Invalid position")

        with self.assertRaises(ValueError) as context:
            move_direction("N", 6, -1)
        self.assertEqual(str(context.exception), "Invalid position")

    def test_direction(self):
        self.assertEqual(move_direction("N", 2, 5) , (2, 4)), "check N"

        actual = move_direction("S", 2, 5)
        self.assertEqual(actual, (2, 6), "check S")

        # ... (other test cases)

    def test_invalid_direction(self):
        try:
            move_direction("XYZ", 7, 5)
        except ValueError as e:
            self.assertEqual(str(e), "Invalid direction")

if __name__ == "__main__":
    unittest.main()
