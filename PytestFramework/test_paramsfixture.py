import pytest


@pytest.mark.usefixtures("crossBrowser")

class TestCrossBrowser:
    def test_data_params_fixture(self,crossBrowser):
        print(crossBrowser)