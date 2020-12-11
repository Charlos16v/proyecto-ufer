from src.services.crawler.web_crawler import crawl_web
import pytest


@pytest.mark.crawl_web
def test_crawl_web():
    assert crawl_web("https://charlos16v.github.io/proyecto-ufer/", 1) == []
    assert crawl_web("https://charlos16v.github.io/proyecto-ufer/", 2) == [
        'https://charlos16v.github.io/proyecto-ufer/./products/ufer_gold.html',
        'https://charlos16v.github.io/proyecto-ufer/./products/ufer_bus.html',
        'https://charlos16v.github.io/proyecto-ufer/./products/ufer_space.html',
        'https://charlos16v.github.io/proyecto-ufer/./products/ufer_business.html',
        'https://charlos16v.github.io/proyecto-ufer/./products/ufer_dailyplus.html',
        'https://charlos16v.github.io/proyecto-ufer/./products/ufer_life.html',
        'https://charlos16v.github.io/proyecto-ufer/./products/ufer_daily.html',
        'https://charlos16v.github.io/proyecto-ufer/./products/ufer_lite.html']
