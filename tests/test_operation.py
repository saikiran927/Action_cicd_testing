from src.maths import add,sub

def test_add():
    assert add(2,3)==5
    assert add(4,3)==7
    assert add(5,3)==8
    
def test_sub():
    assert sub(2,3)==-1
    assert sub(4,3)==1
    assert sub(5,3)==2
    
def test_mul():
    assert mul(2,3)==6
    assert mul(4,3)==12
    assert mul(5,3)==15
    
    