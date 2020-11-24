import requests
from requests.models import Response

#Funcion encargada de hacer un request y obtener el response en forma de string.
def get_content(url):
    contenido = requests.get(url)
    return (contenido.text)


#Test rapido no tener en cuenta.
print (get_content('http://www.udacity.com/cs101x/index.html'))
