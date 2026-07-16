from src.mathsoperators import add,sub

def test_add():
    assert add(2,3)==5
    assert add(5,6)==11
    assert add(5,6)==11
    assert add(5,3)==7

def test_sub():
    assert add(2,3)==-1
    assert add(3,3)==0
    assert add(12,6)==6
