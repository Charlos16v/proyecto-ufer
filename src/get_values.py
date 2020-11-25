from int_detector import int_detector
from string_to_list import string_to_list


UFER_KEYS = ['name', 'description', 'driver', 'passengers', 'privacy', 'seats', 'propulsion', 'top_speed', 'price', 'amenities']


def get_values(content):
    ufer_values = []
    for key in UFER_KEYS:
        id_case=('id="' + str(key)+'">')
        content_pos = content.find(id_case)
        start_pos = content.find(">",content_pos)
        if key != "amenities":
            end_pos=content.find("<",start_pos+1)
            ufer_values.append(int_detector(content[start_pos+1:end_pos]))
        elif key == "amenities":
            end_pos=content.find("</ul",start_pos+1)
            ufer_values.append(string_to_list(content[start_pos+1:end_pos]))
    return ufer_values


#print(get_values(get_content("https://charlos16v.github.io/proyecto-ufer/ufer_bus.html")))



