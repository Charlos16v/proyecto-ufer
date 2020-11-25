# MEJORAR
# Convierte las rutas relativas a otras pàginas, a una url "valida", con su correspondiente dominio.
def repair_link(link):
    if link.find("http://") == -1:
        link="https://charlos16v.github.io/proyecto-ufer/"+link
        return link
    return link
