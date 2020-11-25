import requests

# REVISAR
# Convierte el contenido de los elementos de una lista en un array.
def string_to_list(string):
    list = string.split('</li>')
    list.pop()
    parsed_list = []
    for e in list:
        start_pos=e.find(">")
        parsed_list.append(e[start_pos+1:])
    return parsed_list


# MEJORAR
# Convierte las rutas relativas a otras pàginas, a una url "valida", con su correspondiente dominio.
def repair_link(link):
    if link.find("http://") == -1:
        link="https://charlos16v.github.io/proyecto-ufer/"+link
        return link
    return link


# Funcion encargada de hacer un request y obtener el response en forma de string a partir de <body>.
def get_content(url):
    contenido = requests.get(url)
    contenido = contenido.text
    contenido = contenido.replace("\r","")
    contenido = contenido.replace("\n","")
    body_pos = contenido.find("<body>")
    return (contenido[body_pos:])

#print(get_content("https://charlos16v.github.io/proyecto-ufer/ufer_life.html"))