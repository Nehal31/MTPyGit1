import smtplib
import pytest


class TestClass:

    @pytest.fixture(scope='class', autouse=True)
    def smtp(self, request):
        smtp = smtplib.SMTP("smtp.gmail.com")
        #request.cls.name = self.NAME
        print("creating smtp")

        def fin():
            print("teardown smtp")
            smtp.close()
        request.addfinalizer(fin)
        request.cls.smtp = smtp # provide the fixture value

    def test_ehlo(self):
        smtp = self.smtp
        response, msg = smtp.ehlo()
        assert response == 250
        assert b"smtp.gmail.com" in msg

    def test_noop(self):
        smtp = self.smtp
        response, msg = smtp.noop()
        assert response == 250
        # assert 0  # for demo purposes

