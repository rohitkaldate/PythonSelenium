import pytest


@pytest.fixture(scope="class")
def setup():
    print("This is setup")
    yield
    print("This is teardown, which runs after the test case execution")

@pytest.fixture()
def data():
    print("This is data fixtures test case")
    return ['Rohit','QA',2]

@pytest.fixture(params=["Chrome","Edge","Firefox","Safari","Opera"])
def crossBrowser(request):
    print("This is cross browser test case")
    return request.param