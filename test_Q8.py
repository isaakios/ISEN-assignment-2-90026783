from QuestionEight import move_direction

def test_direction():

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