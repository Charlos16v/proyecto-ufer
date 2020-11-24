# EN OBRAS
from web_crawler import crawl_web,get_page


urls=crawl_web("https://charlos16v.github.io/proyecto-ufer/",3)

#for i in urls:


#contenido=get_page("http://127.0.0.1:5500/ufer/ufer_gold.html")



#def get_next_target(page):
#    start_link = page.find('<h3 id="name"')
#    if start_link == -1:
#        return None, 0
#   start_quote = page.find('"', start_link)
#   end_quote = page.find('"', start_quote + 1)
#   url = page[start_quote + 1:end_quote]
#   return url, end_quote


#name=contenido.find('<h3 id="name"')




