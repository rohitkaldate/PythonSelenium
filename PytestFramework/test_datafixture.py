import pytest


@pytest.mark.usefixtures("data")
class TestData:
    def test_data_fixture(self,data):
        print(data)
        print("Name is: ",data[0])
        print("Designation: ",data[1])