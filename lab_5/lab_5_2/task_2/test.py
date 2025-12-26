from main import unique_elements
import pytest

@pytest.mark.parametrize("lst, expected", [
    ([1, 2, 3], [1, 2, 3]),
    (['a', 'b', 'c'], ['a', 'b', 'c']),
    ([1, 2, 2, 3, 3], [1, 2, 3]),
    (['a', 'a', 'b'], ['a', 'b']),
])
def test_flat_lists(lst, expected):
    assert sorted(unique_elements(lst)) == sorted(expected)

@pytest.mark.parametrize("lst, expected", [
    ([1, [2, 3], 4], [1, 2, 3, 4]),
    ([[1, 2], [3, 4]], [1, 2, 3, 4]),
    ([1, [2, [3, 4]], 5], [1, 2, 3, 4, 5]),
])
def test_nested_lists(lst, expected):
    assert sorted(unique_elements(lst)) == expected

def test_empty_and_nested_empty():
    assert unique_elements([]) == []
    assert unique_elements([[], []]) == []
    assert sorted(unique_elements([[], [1, 2], []])) == [1, 2]

def test_mixed_data_types():
    result = unique_elements([1, 'hello', [2, 'world'], 1, 'hello'])
    assert set(result) == {1, 2, 'hello', 'world'}

@pytest.mark.xfail
def test_dict_inside_list():
    unique_elements([1, {'a': 1}, [2, {'b': 2}]])

@pytest.mark.skip
def test_input_list_not_modified():
    data = [1, [2, 3]]
    unique_elements(data)
    assert data == [1, [2, 3]]

def test_single_element():
    assert unique_elements([42]) == [42]

def test_all_duplicates():
    assert unique_elements([1, 1, [1, [1]], 1]) == [1]
