# This function takes a direction and a position and returns the new position
def move_direction(direction, x, y):
    if x < 0 or y < 0 or x > 7 or y > 7:
        raise ValueError('Invalid position')
    if direction == 'N':
        y -= 1
    elif direction == 'S':
        y += 1
    elif direction == 'E':
        x += 1
    elif direction == 'W':
        x -= 1
    elif direction == 'NE':
        x += 1
        y -= 1
    elif direction == 'NW':
        x -= 1
        y -= 1
    elif direction == 'SE':
        x += 1
        y += 1
    elif direction == 'SW':
        x -= 1
        y += 1
    else:
        raise ValueError('Invalid direction')
    return x, y
    
#your code below this line ----------------------------
import unittest


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

        # Test North ('N')
        self.assertEqual(move_direction("N", 2, 5) , (2, 4)), "Failed for 'N'"

        # Test South ('S')
        self.assertEqual(move_direction("S", 2, 5) , (2, 6)), "Failed for 'S'"

        # Test East ('E')
        self.assertEqual(move_direction("E", 2, 5) , (3, 5)), "Failed for 'E'"

        # Test West ('W')
        self.assertEqual(move_direction("W", 2, 5) , (1, 5)), "Failed for 'W'"

        # Test North-East ('NE')
        self.assertEqual(move_direction("NE", 2, 5) , (3, 4)), "Failed for 'NE'"

        # Test North-West ('NW')
        self.assertEqual(move_direction("NW", 2, 5) , (1, 4)), "Failed for 'NW'"

        # Test South-East ('SE')
        self.assertEqual(move_direction("SE", 2, 5) , (3, 6)), "Failed for 'SE'"

        # Test South-West ('SW')
        self.assertEqual(move_direction("SW", 2, 5) , (1, 6)), "Failed for 'SW'"


    def test_invalid_direction(self):
        with self.assertRaises(ValueError) as context:
            move_direction("XYZ", 7, 5)
        self.assertEqual(str(context.exception), "Invalid direction")

if __name__ == "__main__":
    unittest.main()
