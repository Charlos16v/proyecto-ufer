# CONFIGURACIÓN PARA EL SCRAPPER DE UFER


# En "UFER_URI se declara la conexion al cluster de mongoDB."
UFER_URI = "mongodb+srv://charlos:Ufer69@cluster0.35hqi.mongodb.net/Ufer?retryWrites=true&w=majority"


# En "UFER_DOMAIN" se declara el dominio de la web a scrappear.
UFER_DOMAIN = "https://charlos16v.github.io/proyecto-ufer/"


# En "UFER_DEPTH" se define la profundidad de la recursividad de búsqueda de links.
UFER_DEPTH = 3


# En "UFER_KEYS" se define el respectivo identificador del contenido a scrappear.
UFER_KEYS = ['name', 'description', 'driver', 'passengers', 'privacy', 'seats', 'propulsion', 'top_speed', 'price', 'amenities']

# UFER_KEYS = ['name', 'description', 'price']

# UFER_KEYS = ['name', 'amenities', 'price'] # DESACTIVAR SCHEMA

# En "UFER_TYPE" se define el respectivo type del contenido a scrappear.
UFER_TYPE = [str, str, str, int, str, str, str, int, int, list]

# UFER_TYPE = [str, str, int]

# UFER_TYPE = [str, list, int] # DESACTIVAR SCHEMA

assert len(UFER_TYPE) == len(UFER_KEYS) # precondición para comprobar que las 2 listas tienen la misma longitud.