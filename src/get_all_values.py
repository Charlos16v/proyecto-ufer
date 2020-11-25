# En Obras
#links=crawl_web("https://charlos16v.github.io/proyecto-ufer/",3)
###

#print(links)

###
def get_values_on_links(links):
    datos=[]
    for link in links:
        datos.append((get_values(get_content(link))))
    return datos
###

#print(get_values_on_links(links))