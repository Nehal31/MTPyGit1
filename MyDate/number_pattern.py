import pytest
import re

def single(a, b):
    diff = abs(b - a)
    print("Diff", diff)
    num1 = "%03d" % a
    num2 = "%03d" % b

    ln = len(num1) - 1
    if diff < 10:
        n1_once = int(num1[ln])
        n2_once = int(num2[ln])
        if n1_once < n2_once:
            reg = "%s[%d-%d]" %(num1[ln-1], n1_once, n2_once)
        else:
            reg = "(%d[%d-%d]|%d[%d-%d])" % (int(num1[ln-1]), n1_once,
                                             9, int(num1[ln-1])+1,
                                             0, n2_once)
    elif 10 <= diff < 60:
        n1_once = int(num1[ln])
        n2_once = int(num2[ln])

        n1_dec = int(num1[ln-1])
        n2_dec = int(num2[ln-1])

        if int(num1[ln - 1:]) < int(num2[ln - 1:]):
            first = "%d[%d-%d]" % (n1_dec, n1_once, 9)
            last = "%d[%d-%d]" % (n2_dec, 0, n2_once)
            if n2_dec - n1_dec >= 2:
                mid = "[%d-%d]\d" % (n1_dec+1, n2_dec-1)
                reg = "(%s|%s|%s)" % (first, mid, last)
            else:
                reg = "(%s|%s)" % (first, last)
        else:
            first = single(int(num1), 59)
            last = single(0, int(num2))

            prev1 = int(num1[ln - 2])
            prev2 = int(num2[ln - 2])

            if prev1 == prev2:
                reg = "%d(%s|%s)" % (prev1, first, last)
            elif prev2 - prev1 < 2:
                reg = "(%d%s|%d%s)" % (prev1, first, prev2, last)
            else:
                reg = "(%d%s|[%d-%d][0-5]\d|%d%s)" % (prev1, first, prev1 + 1,
                                                      prev2 - 1, prev2, last)
            #reg = "(%s|%s)" % (first, last)

    return reg

def test_single():
    print("Test1 %d , %d" % (11, 17))
    res = single(11, 17)
    print(res)
    assert res == r'1[1-7]'
    assert re.search(res, '16')
    assert not re.search(res, '06')
    assert not re.search(res, '61')
    print("Test1 Done")

    print("Test2 %d , %d" % (14, 23))
    res = single(14, 23)
    print(res)
    assert res == r'(1[4-9]|2[0-3])'
    assert re.search(res, '16')
    assert re.search(res, '23')
    assert not re.search(res, '06')
    assert not re.search(res, '61')
    print("Test2 Done")

    print("Test3 %d , %d" % (14, 33))
    res = single(14, 33)
    print(res)
    assert res == r'(1[4-9]|[2-2]\d|3[0-3])'
    assert re.search(res, '16')
    assert re.search(res, '33')
    assert not re.search(res, '06')
    assert not re.search(res, '61')
    print("Test3 Done")

    print("Test4 %d , %d" % (44, 59))
    res = single(44, 59)
    print(res)
    assert res == r'(4[4-9]|5[0-9])'
    assert re.search(res, '46')
    assert re.search(res, '59')
    assert not re.search(res, '06')
    assert not re.search(res, '65')
    print("Test4 Done")

    print("Test5 %d , %d" % (54, 28))
    res = single(54, 28)
    print(res)
    """
    assert res == r'(5[4-9]|(0[0-9]|[1-1]\d|2[0-8]))'
    assert re.search(res, '156')
    assert re.search(res, '228')
    assert not re.search(res, '38')
    assert not re.search(res, '53')
    print("Test5 Done")

    print("Test6 %d , %d" % (44, 32))
    res = single(44, 32)
    print(res)
    #assert res == r'(5[4-9]|(0[0-9]|[1-1]\d|2[0-8]))'
    print("Test5 Done")
    """


if __name__ == '__main__':
    test_single()