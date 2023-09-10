from QuestionEight import move_direction

def test_invalid_position():
    # expecting a ValueError, learn it from this website https://pytest-with-eric.com/introduction/pytest-assert-exception/
    try:
        move_direction("N", 8, 5)
    except ValueError as e:
        assert str(e) == "Invalid position"

    try:
        move_direction("S", 6, 8)
    except ValueError as e:
        assert str(e) == "Invalid position"

    try:
        move_direction("N", -1, 5)
    except ValueError as e:
        assert str(e) == "Invalid position"

    try:
        move_direction("N", 6, -1)
    except ValueError as e:
        assert str(e) == "Invalid position"

    print("test invalid direction passed")

def test_direction():

    # all directions
    actual = move_direction("N", 2, 5)
    assert actual == (2, 4) , "check N"

    actual = move_direction("S", 2, 5)
    assert actual == (2, 6), "check S"

    actual = move_direction("E", 2, 5)
    assert actual == (3, 5), "check E"
    
    actual = move_direction("W", 2, 5)
    assert actual == (1, 5), "check W"
    
    actual = move_direction("NE", 2 , 5)
    assert actual == (3, 4), "check NE"

    actual = move_direction("NW", 2 , 5)
    assert actual == (1, 4), "check NW"

    actual = move_direction("SE", 2, 5)
    assert actual == (3 , 6), "check SE"
    
    actual = move_direction("SW", 2 , 5)
    assert actual == (1, 6), "check SW"

    print("test all direction passed")

def test_invalid_direction():
    try:
        move_direction("XYZ", 7, 5)
    except ValueError as e:
        assert str(e) == "Invalid direction"
    except AssertionError:
        pass
    print("test invalid direction passed")
    
if __name__ == "__main__":
    test_invalid_position()
    test_direction()
    test_invalid_direction()