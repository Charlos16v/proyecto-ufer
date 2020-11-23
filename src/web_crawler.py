# EN FUNCIONAMIENTO

import requests
from requests.models import Response


# repair_link se encarga de transformar los enlaces a ficheros "about.html" en un enlace con http:// y el respectivo dominio.

def repair_link(link):
    if link.find("http://") == -1:
        link="http://127.0.0.1:5500/ufer/"+link
        return link
    return link


# get_page se encarga de hacer un request a la url indicada, devolviendo un response con el contenido html.

def get_page(url):
    contenido = requests.get(url)
    return (contenido.text)


# get_next_target recorre el contenido HTML en busca de enlaces "<a href=" y devuelve enlaces y su posicion final.

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


# union se encarga de insertar el contenido de la lista "q" que no se encuentra en "p".

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)


# get_all_links se encarga de extraer

def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            parsed_url=repair_link(url)
            links.append(parsed_url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed,max_depth):
    tocrawl = [seed]
    crawled = []
    next_depth = []
    depth = 0
    while tocrawl and depth <= max_depth:
        page = tocrawl.pop()
        if page not in crawled:
            union(next_depth, get_all_links(get_page(page)))
            crawled.append(page)
        if not tocrawl:
            tocrawl, next_depth = next_depth, []
            depth += 1
    return crawled


print(crawl_web("http://127.0.0.1:5500/ufer/services.html",2))




