# content of conftest.py

import smtplib
import pytest

@pytest.fixture(scope='module', autouse=True)
def smtp(request):
    smtp = smtplib.SMTP("smtp.gmail.com")
    print("creating smtp")

    def fin():
        print("teardown smtp")
        smtp.close()
    request.addfinalizer(fin)
    return smtp  # provide the fixture value

