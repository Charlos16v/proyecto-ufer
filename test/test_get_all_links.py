from requests.api import get
from src.services.crawler.web_crawler import get_all_links,get_content
import pytest


@pytest.mark.get_all_links
def test_get_all_links():
    assert get_all_links(get_content("https://charlos16v.github.io/proyecto-ufer/")) == ['https://charlos16v.github.io/proyecto-ufer/index.html', 'https://charlos16v.github.io/proyecto-ufer/#', 'https://charlos16v.github.io/proyecto-ufer/services.html', 'https://charlos16v.github.io/proyecto-ufer/about.html', 'https://charlos16v.github.io/proyecto-ufer/services.html']
    assert get_all_links(get_content("https://charlos16v.github.io/proyecto-ufer/services.html")) == ['https://charlos16v.github.io/proyecto-ufer/index.html', 'https://charlos16v.github.io/proyecto-ufer/index.html', 'https://charlos16v.github.io/proyecto-ufer/#', 'https://charlos16v.github.io/proyecto-ufer/about.html', 'https://charlos16v.github.io/proyecto-ufer/./products/ufer_lite.html', 'https://charlos16v.github.io/proyecto-ufer/./products/ufer_daily.html', 'https://charlos16v.github.io/proyecto-ufer/./products/ufer_life.html', 'https://charlos16v.github.io/proyecto-ufer/./products/ufer_dailyplus.html', 'https://charlos16v.github.io/proyecto-ufer/./products/ufer_business.html', 'https://charlos16v.github.io/proyecto-ufer/./products/ufer_space.html', 'https://charlos16v.github.io/proyecto-ufer/./products/ufer_bus.html', 'https://charlos16v.github.io/proyecto-ufer/./products/ufer_gold.html']
    assert get_all_links(get_content("https://www.google.com/")) == []