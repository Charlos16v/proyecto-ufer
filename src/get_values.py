from web_crawler import crawl_web
from mini_tools import string_to_list,get_content


ufer_keys = ['name', 'description', 'driver', 'passengers', 'privacy', 'seats', 'propulsion', 'top_speed', 'price', 'amenities']


def get_values(content):
    ufer_values = []
    for key in ufer_keys:
        id_case=('id="' + str(key)+'">')
        content_pos = content.find(id_case)
        start_pos = content.find(">",content_pos)
        if key != "amenities":
            end_pos=content.find("<",start_pos+1)
            ufer_values.append(content[start_pos+1:end_pos])
        elif key == "amenities":
            end_pos=content.find("</ul",start_pos+1)
            ufer_values.append(string_to_list(content[start_pos+1:end_pos]))
    return ufer_values



# En Obras

###
#links=crawl_web("https://charlos16v.github.io/proyecto-ufer/",3)
#datos=[]
#for i in links:
#    datos.append((get_values(get_content(i))))
#print(datos)
###



