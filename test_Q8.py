from QuestionEight import move_direction

def test_direction():

    # expecting a ValueError, learn it from this website https://pytest-with-eric.com/introduction/pytest-assert-exception/
    try:
        move_direction("N", 7, 5)
    except ValueError as e:
        assert str(e) == "Invalid x>7 expected"

    try:
        move_direction("S", 6, 7)
    except ValueError as e:
        assert str(e) == "Invalid y>7 expected"

    try:
        move_direction("N", 0, 5)
    except ValueError as e:
        assert str(e) == "Invalid x<0 expected"

    try:
        move_direction("N", 6, 0)
    except ValueError as e:
        assert str(e) == "Invalid y<0 expected"
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

    print("test passed")

test_direction()