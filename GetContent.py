import requests
from requests.models import Response

#Funcion encargada de hacer un request y obtener el response en forma de string.
def GetContent(url):
    contenido = requests.get(url)
    return (contenido.content)


#Test rapido no tener en cuenta.
print (GetContent('http://127.0.0.1:5500/testscrapper.html'))

def get_content(url):

