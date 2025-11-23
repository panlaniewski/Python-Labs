from main import merge_dicts

def test_simple_merge():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    merge_dicts(dict1, dict2)
    assert dict1 == {'a': 1, 'b': 2, 'c': 3, 'd': 4}

def test_overwrite_same_type():
    dict1 = {'a': 1, 'b': 'hello'}
    dict2 = {'a': 2, 'b': 'world'}
    merge_dicts(dict1, dict2)
    assert dict1 == {'a': 2, 'b': 'world'}

def test_numeric_max():
    dict1 = {'a': 5, 'b': 10.5}
    dict2 = {'a': 10, 'b': 5.5}
    merge_dicts(dict1, dict2)
    assert dict1 == {'a': 10, 'b': 10.5}

def test_different_types_list():
    dict1 = {'a': 'hello', 'b': 42}
    dict2 = {'a': 123, 'b': 'world'}
    merge_dicts(dict1, dict2)
    assert dict1 == {'a': ['hello', 123], 'b': [42, 'world']}

def test_recursive_dict_merge():
    dict1 = {'a': 1, 'nested': {'x': 10, 'y': 20}}
    dict2 = {'b': 2, 'nested': {'y': 30, 'z': 40}}
    merge_dicts(dict1, dict2)
    assert dict1 == {'a': 1, 'b': 2, 'nested': {'x': 10, 'y': 30, 'z': 40}}

def test_deeply_nested_dicts():
    dict1 = {'level1': {'level2': {'level3': {'a': 1}}}}
    dict2 = {'level1': {'level2': {'level3': {'b': 2}}}}
    merge_dicts(dict1, dict2)
    expected = {'level1': {'level2': {'level3': {'a': 1, 'b': 2}}}}
    assert dict1 == expected

def test_mixed_nested_operations():
    dict1 = {'data': {'num': 5, 'text': 'hello', 'mixed': 10}}
    dict2 = {'data': {'num': 8, 'text': 'world', 'mixed': 'string'}}
    merge_dicts(dict1, dict2)
    assert dict1 == {'data': {'num': 8, 'text': 'world', 'mixed': [10, 'string']}}

def test_empty_dicts():
    dict1 = {}
    dict2 = {'a': 1}
    merge_dicts(dict1, dict2)
    assert dict1 == {'a': 1}
    
    dict1 = {'a': 1}
    dict2 = {}
    original_dict1 = dict1.copy()
    merge_dicts(dict1, dict2)
    assert dict1 == original_dict1  

def test_none_values():
    dict1 = {'a': None, 'b': 10}
    dict2 = {'a': 'value', 'b': None}
    merge_dicts(dict1, dict2)
    assert dict1 == {'a': [None, 'value'], 'b': [10, None]}

def test_list_values():
    dict1 = {'items': [1, 2, 3], 'data': {'nums': [1, 2]}}
    dict2 = {'items': [4, 5, 6], 'data': {'nums': [3, 4]}}
    merge_dicts(dict1, dict2)
    assert dict1 == {'items': [4, 5, 6], 'data': {'nums': [3, 4]}}

def test_tuple_values():
    dict1 = {'coord': (1, 2), 'value': 10}
    dict2 = {'coord': (3, 4), 'value': 20}
    merge_dicts(dict1, dict2)
    assert dict1 == {'coord': (3, 4), 'value': 20}  

def test_set_values():
    dict1 = {'items': {1, 2, 3}}
    dict2 = {'items': {3, 4, 5}}
    merge_dicts(dict1, dict2)
    assert dict1 == {'items': {3, 4, 5}}  