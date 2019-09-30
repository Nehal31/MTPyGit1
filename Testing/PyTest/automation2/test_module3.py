import pytest
import datetime as dt


class TestClass:
    @pytest.fixture(scope='class', autouse=True)
    def setup_cleanup(self, request):
        request.cls.date = dt.datetime.now()
        request.cls.voter_age = 18
        request.cls.voter = []
        #name = self.get_param('name', "Default Name")
        print("Start Voting...", request.cls.voter)
        def fin():
            request.cls.voter.clear()
            print("Voting Done. Remove Voters", request.cls.voter)
        request.addfinalizer(fin)


    @pytest.fixture(scope='function', autouse=True)
    def printer(self, request):
        print("Voter List :")
        print("Before : ", request.cls.voter)
        yield
        print("After : ", request.cls.voter)


    def test_voter1(self):
        age = 21
        name = "ABC"
        assert age >= self.voter_age
        self.voter.append([name, age])

    def test_voter2(self):
        age = 18
        name = "XYZ"
        assert age >= self.voter_age
        self.voter.append([name, age])

