import pytest
#test_TC001_FirstTestCase.py
a = 100
b = 100
@pytest.fixture(scope="module")
def fixture_demo():
    print("Fixture example............")
    print("...........................")
    yield
    print("Close this damned thing ..would ya..")
    print("..................................")

@pytest.mark.Smoke
@pytest.mark.Regression
def test_tc001_login_logout(fixture_demo):
    print("This is out test case code.....")
    print("The first test case...")
    assert a != b,"These two value must not be same"
@pytest.mark.Regression
def test_tc001_login_logout_registration(fixture_demo):
    print("This is out test case code.....")
    print("The second test case...")
