#!pytest

import pytest
import logging


class TestClass:
    @pytest.fixture(scope='class', autouse=True)
    def setup_cleanup1(self):
        print("Create volume 1")
        yield
        print("Delete volume 1")


    def test_01(self):
        print("this is my testcase")

    def test_02(self):
        print("this is my testcase 2")


class TestClass2:

    @pytest.fixture(scope='class', autouse=True)
    def setup_cleanup(self, request):
        print("Inside setup_cleanup", request)
        request.conn = True
        self.name = "ABC"
        def fin():
            request.conn = None
        return request.addfinalizer(fin)
        print("Exiting setup_cleanup")

    def test_t01(self):
        print("Inside test_t01")
        #print(self.name)
        print("Exiting t01")


if __name__ == '__main__':
    pytest.main([__file__])

