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