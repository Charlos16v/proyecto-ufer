from src.services.scrapper.int_detector import int_detector
import pytest

@pytest.mark.int_detector
def test_int_detector():
    assert int_detector('789') == 789
    assert int_detector('hello') == 'hello'
    assert int_detector('a1b2c3') == 'a1b2c3'
    assert int_detector('1111111a') == '1111111a'
    assert int_detector('1111111a') == '1111111a'
    assert int_detector(8) == 8

