import pytest


@pytest.mark.usefixtures("setup")
class TestFixtureExample:

    def test_fixture_example(self) :
        print("This is fixture example and executes fixture methods")

    def test_fixture_example1(self) :
        print("This is fixture example1 and executes fixture methods")

    def test_fixture_example2(self) :
        print("This is fixture example2 and executes fixture methods")

    def test_fixture_example3(self) :
        print("This is fixture example3 and executes fixture methods")

    def test_fixture_example4(self) :
        print("This is fixture example4` and executes fixture methods")