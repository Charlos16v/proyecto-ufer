from src.services.scrapper.make_dictionary import make_dictionary
import pytest

@pytest.mark.make_dictionary
def test_make_dictionary():
    assert make_dictionary([1, 2, 3], ['uno', 'dos', 'tres']) == {1:'uno', 2:'dos', 3:'tres'}
    assert make_dictionary('a', 'b') == {'a': 'b'}
    assert make_dictionary([1, 2, 3], ['uno', 'dos']) == {1:'uno', 2:'dos'}
    assert make_dictionary([],[]) == {}
