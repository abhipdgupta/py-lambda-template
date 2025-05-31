from src.math.add import add_custom


def test_add1():
    assert add_custom(1, 2, 3) == 6

def test_add2():
    assert add_custom(1, 2, 3, 4) == 10

def test_add3():
    assert add_custom(1, 2, 3, 4, 5) == 15
    
def test_add4():
    assert not add_custom(1, 2, 3, 4, 5, 6) != 21
