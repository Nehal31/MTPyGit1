import math
import logging as log
import pytest

logFormat = " %(asctime)s: %levelname(s) => %(message)s, datefmt='%Y-%b-%d %I:%M:%S %p"
log.basicConfig(filename='mylog.txt', level=log.INFO, format=logFormat, filemode='a+')


num = 25


def setup_cleanup():
   global num
   num = 20

@pytest.mark.square
def test_sqrt():
   num = 25
   log.debug(num)
   assert math.sqrt(num) == 5


@pytest.mark.square
def testsquare():
   num = 7
   log.debug(num)
   assert 7*7 == 40


@pytest.mark.other
def testequality():
   assert 10 == 10


@pytest.mark.other
def testnotequality():
   assert 10 == 11