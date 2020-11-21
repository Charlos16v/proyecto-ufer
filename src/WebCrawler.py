# EN FASE DE PRUEBAS

import requests
from requests.models import Response


def get_content(url):
    contenido = requests.get(url)
    return (contenido.text)

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl,get_all_links(get_content(page)))
            crawled.append(page)
    return crawled

#print (get_content(crawl_web("http://127.0.0.1:5500/testscrapper.html")))

print (crawl_web("http://127.0.0.1:8000"))




