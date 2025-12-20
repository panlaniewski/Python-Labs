from main import merge_dicts
import pytest

@pytest.mark.parametrize("d1, d2, expected", [
    ({'a': 1}, {'b': 2}, {'a': 1, 'b': 2}),
    ({'a': 'x'}, {'a': 'y'}, {'a': 'y'}),
    ({'a': 5}, {'a': 10}, {'a': 10}),
    ({'a': 10.5}, {'a': 5.5}, {'a': 10.5}),
    ({'a': 1}, {'a': 'x'}, {'a': [1, 'x']}),
    ({'n': {'x': 1}}, {'n': {'y': 2}}, {'n': {'x': 1, 'y': 2}}),
])
def test_core_logic(d1, d2, expected):
    merge_dicts(d1, d2)
    assert d1 == expected

def test_deep_nested_merge():
    d1 = {'a': {'b': {'c': 1}}}
    d2 = {'a': {'b': {'d': 2}}}
    merge_dicts(d1, d2)
    assert d1 == {'a': {'b': {'c': 1, 'd': 2}}}

def test_mixed_nested_types():
    d1 = {'data': {'num': 5, 'val': 10}}
    d2 = {'data': {'num': 3, 'val': 'x'}}
    merge_dicts(d1, d2)
    assert d1 == {'data': {'num': 5, 'val': [10, 'x']}}

def test_empty_dicts():
    d1 = {}
    merge_dicts(d1, {'a': 1})
    assert d1 == {'a': 1}

    d2 = {'a': 1}
    merge_dicts(d2, {})
    assert d2 == {'a': 1}

@pytest.mark.xfail
def test_none_values():
    d1 = {'a': None}
    d2 = {'a': 1}
    merge_dicts(d1, d2)
    assert d1 == {'a': 1}

@pytest.mark.skip(reason="Списки, множества и кортежи перезаписываются")
def test_collections_merge():
    d1 = {'x': [1, 2], 'y': {1, 2}}
    d2 = {'x': [3], 'y': {3}}
    merge_dicts(d1, d2)
    assert d1 == {'x': [1, 2, 3], 'y': {1, 2, 3}}

def test_collections_overwrite():
    d1 = {'items': [1, 2], 'coord': (1, 2), 'set': {1, 2}}
    d2 = {'items': [3], 'coord': (3, 4), 'set': {3}}
    merge_dicts(d1, d2)
    assert d1 == {'items': [3], 'coord': (3, 4), 'set': {3}}
