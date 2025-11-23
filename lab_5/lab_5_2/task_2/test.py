from main import unique_elements

def test_flat_list_no_duplicates():
    assert sorted(unique_elements([1, 2, 3])) == [1, 2, 3]
    assert sorted(unique_elements(['a', 'b', 'c'])) == ['a', 'b', 'c']

def test_flat_list_with_duplicates():
    assert sorted(unique_elements([1, 2, 2, 3, 3, 3])) == [1, 2, 3]
    assert sorted(unique_elements(['a', 'a', 'b', 'b', 'b'])) == ['a', 'b']
    
def test_nested_list_one_level():
    assert sorted(unique_elements([1, [2, 3], 4])) == [1, 2, 3, 4]
    assert sorted(unique_elements([[1, 2], [3, 4]])) == [1, 2, 3, 4]
    
def test_deeply_nested_list():
    assert sorted(unique_elements([1, [2, [3, 4]], 5])) == [1, 2, 3, 4, 5]
    assert sorted(unique_elements([[[1, 2]], [3, [4, 5]]])) == [1, 2, 3, 4, 5]
    
def test_nested_list_with_duplicates():
    assert sorted(unique_elements([1, [1, 2], 2, [3, 3]])) == [1, 2, 3]
    assert sorted(unique_elements([[1, 1], [2, [1, 2]], 3])) == [1, 2, 3]
    
def test_empty_list():
    assert unique_elements([]) == []

def test_nested_empty_lists():
    assert sorted(unique_elements([[], [1, 2], []])) == [1, 2]
    assert unique_elements([[], []]) == []  
    
def test_mixed_data_types():
    result = unique_elements([1, 'hello', [2, 'world'], 1, 'hello'])
    assert set(result) == {1, 2, 'hello', 'world'}
    assert len(result) == 4  
    
def test_complex_nested_structure():
    input_list = [1, [2, [3, [4, 5]]], [6, 7], 1, [2, 3]]
    result = unique_elements(input_list)
    assert sorted(result) == [1, 2, 3, 4, 5, 6, 7]
    
def test_single_element():
    assert unique_elements([42]) == [42]
    assert unique_elements([['nested']]) == ['nested']

def test_all_duplicates():
    assert unique_elements([1, 1, [1, [1]], 1]) == [1]
    assert unique_elements([['a'], 'a', ['a']]) == ['a']
    
    