import pytest







@pytest.fixture(scope='class')
def print_filename():
    print("***Module name: {}".format(__name__))
    print("***Hello Module")



class TestClass:
    @pytest.fixture(scope='class')
    def get_module_name(self):
        return __name__

    def test_01(self, print_filename, get_module_name):
        print("***this is my testcase")
        print("***Inside testcase, module name: {}".format(get_module_name))
