from src.services.crawler.union import union


@pytest.mark.union
def test_union():
    assert union(['a', 'b', 'c'], ['c', 'd', 'e']) == ['a', 'b', 'c', 'd', 'e']