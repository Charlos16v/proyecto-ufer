from services.src.scrapper.scrapp import scrapp
from services.src.crawler.get_content import get_content
from services.src.config.ufer_conf import UFER_DEPTH, UFER_DOMAIN, UFER_KEYS
from services.src.scrapper.make_dictionary import make_dictionary
from repository.to_mongo import to_mongo
from services.src.crawler.web_crawler import crawl_web

def get_values_on_links(links):
    for url in links:
        to_mongo(make_dictionary(UFER_KEYS,scrapp(get_content(url))))


# get_values_on_links(crawl_web(UFER_DOMAIN,UFER_DEPTH))
def get_all_data(url,depth):
    get_values_on_links(crawl_web(url,depth))


get_all_data(UFER_DOMAIN,UFER_DEPTH)


