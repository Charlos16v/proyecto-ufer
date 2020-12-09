from src.repository.to_mongo import to_mongo
from src.services.config.ufer_conf import UFER_KEYS,UFER_DOMAIN,UFER_DEPTH
from src.services.crawler.get_content import get_content
from src.services.crawler.web_crawler import crawl_web
from src.services.scrapper.make_dictionary import make_dictionary
from src.services.scrapper.scrapp import scrapp


def get_values_on_links(links):
    total = []
    for url in links:
        content = make_dictionary(UFER_KEYS, scrapp(get_content(url)))
        total.append(content)
        to_mongo(content)
    return total

def get_all_data(url, depth):
    get_values_on_links(crawl_web(url, depth))
