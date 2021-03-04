import exercice_2
import pytest
@pytest.fixture
def my_set_fixture():
    return set([-1,1,2,3])
def test_add_elem(my_set_fixture):
    oldlength = len(list(my_set_fixture))
    res = exercice_2.add_element(my_set_fixture, -2)
    assert oldlength == len(list(res))
    res = exercice_2.add_element(my_set_fixture, 10)
    assert oldlength < len(list(res))
def test_remove_val(my_set_fixture):
    res = exercice_2.remove_negative_values(my_set_fixture)
    for i in list(res):
        assert i >= 0
    assert list(res) == [1,2,3]
def test_sum(my_set_fixture):
    res = exercice_2.sumset(my_set_fixture)
    assert 5 == res

  