from src.mathsoperators import add,sub

def test_add():
    assert add(2,3)==5
    assert add(5,6)==11
    assert add(5,10)==15
    assert add(5,3)==8

def test_sub():
    assert sub(2,3)==-1
    assert sub(3,3)==0
    assert sub(12,6)==6
