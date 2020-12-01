from services.src.get_values import get_values
from services.src.get_content import get_content
from services.src.get_values_conf import UFER_KEYS,UFER_DOMAIN,UFER_DEPTH
from services.src.make_dictionary import make_dictionary
from services.src.web_crawler import crawl_web
from services.src.to_mongo import to_mongo

# En Obras
#links=crawl_web("https://charlos16v.github.io/proyecto-ufer/",3)
###

#print(links)

###
def get_values_on_links(links):
    for url in links:
        to_mongo(make_dictionary(UFER_KEYS,get_values(get_content(url))))
###

#print(get_values_on_links(links))

get_values_on_links(crawl_web(UFER_DOMAIN,UFER_DEPTH))