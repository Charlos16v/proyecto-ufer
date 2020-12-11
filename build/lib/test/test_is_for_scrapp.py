from src.services.crawler.web_crawler import is_for_scrapp,get_content
import pytest


@pytest.mark.is_for_scrapp
def test_is_for_scrapp():
    assert is_for_scrapp("https://charlos16v.github.io/proyecto-ufer/") == False
    assert is_for_scrapp("https://charlos16v.github.io/proyecto-ufer/about.html") == False
    assert is_for_scrapp("https://charlos16v.github.io/proyecto-ufer/products/ufer_gold.html") == True
    assert is_for_scrapp("https://charlos16v.github.io/proyecto-ufer/products/ufer_lite.html") == True
    assert is_for_scrapp("https://www.google.com/") == False