import requests
# Funcion encargada de hacer un request y obtener el response en forma de string a partir de <body>.
def get_content(url):
    contenido = requests.get(url).text.replace("\r\n","\r").replace("\r","").replace("\n","").replace("\t","") #
    assert contenido == str(contenido) # precondición para comprobar que contenido es un string.
    return (contenido[contenido.find("<body>"):])