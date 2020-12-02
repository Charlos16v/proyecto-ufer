# MEJORAR
# Convierte las rutas relativas a otras pàginas, a una url "valida", con su correspondiente dominio.
from .get_values_conf import UFER_DOMAIN


def repair_link(link):
    if link.find("http://") == -1:
        link=UFER_DOMAIN+link
        return link
    return link
