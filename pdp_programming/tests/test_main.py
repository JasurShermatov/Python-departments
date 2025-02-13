from src.main import func, Logic


def test():
    assert 1==1



def test_func():
    assert func(4)==5
    assert func(9)==10


def test_logic():
    assert Logic.logic_param==10