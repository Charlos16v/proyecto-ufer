from src.services.crawler.web_crawler import union
import pytest

@pytest.mark.union
def test_union():
    assert union(['a', 'b', 'c'], ['c', 'd', 'e']) == union(['a', 'b', 'c', 'd', 'e'], ['c', 'd', 'e'])
    assert union([1, 2, 3], [3, 4, 5]) == union([1, 2, 3, 4, 5], [1, 2, 3])
    assert union([], []) == union([], [])