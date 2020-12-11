from src.services.crawler.web_crawler import get_next_target
import pytest


@pytest.mark.get_next_target
def test_get_next_target():
    assert get_next_target('<body> <a href="master"></a> <a href="test">') == ('master', 22)
    assert get_next_target("") == (None, 0)
    assert get_next_target("hello world") == (None, 0)
