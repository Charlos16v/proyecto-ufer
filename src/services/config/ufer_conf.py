# CONFIGURACIÓN PARA EL SCRAPPER DE UFER

# En "UFER_DOMAIN" se declara el dominio de la web a scrappear.
UFER_DOMAIN = "https://charlos16v.github.io/proyecto-ufer/"


# En "UFER_DEPTH" se define la profundidad de la recursividad de búsqueda de links.
UFER_DEPTH = 3


# En "UFER_KEYS" se define el respectivo identificador del contenido a scrappear.
UFER_KEYS = ['name', 'description', 'driver', 'passengers', 'privacy', 'seats', 'propulsion', 'top_speed', 'price', 'amenities']

# En "UFER_TYPE" se define el respectivo type del contenido a scrappear.
UFER_TYPE = [str, str, str, int, str, str, str, int, int, list]

assert len(UFER_TYPE) == len(UFER_KEYS) # precondición para comprobar que las 2 listas tienen la misma longitud.