import pytest

@pytest.fixture()
def get_val():
    num = 10
    return num


def test_div10(get_val):
    assert get_val // 10 == 1


def test_div5(get_val):
    assert get_val // 5 == 3


def test_div6(get_val):
    assert get_val // 6 == 1