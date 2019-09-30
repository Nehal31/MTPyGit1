import pytest
from my_main_module import my_math


def setup_module():
    pass



def test_add1():
    a = 10
    b = 20
    mm = my_math(a, b)
    mm.set_ready()
    assert mm.add() == 30

def test_add2():
    a = 10
    b = 20
    mm = my_math(a, b)
    assert mm.add() == None

def test_div1():
    a = 10
    b = 2
    mm = my_math(a, b)
    mm.set_ready()
    assert mm.div() == 5.0

def test_div2():
    a = 10
    b = 0
    mm = my_math(a, b)
    mm.set_safe_state
    assert mm.div() == None

