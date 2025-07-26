import pytest


@pytest.mark.smoke
def test_smoke_example(setup):
    print("This is smoke test example with the mark tag")

@pytest.mark.skip
def test_skipping_example():
    print("This is skipping example with the mark tag")