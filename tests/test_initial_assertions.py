import pytest

@pytest.mark.sanity
def test_01():
    assert 5 + 5 == 10

@pytest.mark.smoke
def test_02():
    assert "Hello" == "Hello"

#PARAMETRIZE
@pytest.mark.parametrize("test_input", [82, 10, 0, 5, 6])
def test_param01(test_input):
    assert test_input > 50


# FIXTURES
@pytest.fixture()
def setup_list() -> str:
    print("\n Fixtures ...  ")
    city = ["New York", "London", "Riyadh", "Mexico City"]
    return city

def test_using_fixtures(setup_list):
    print(setup_list[:])
    assert setup_list[0] == "New York"
    assert setup_list[::2] == ["New York", "Riyadh"]
