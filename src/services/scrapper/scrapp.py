from src.services.scrapper.make_dictionary import make_dictionary
from src.services.scrapper.int_detector import int_detector
from src.services.scrapper.string_to_list import string_to_list
from src.services.config.ufer_conf import UFER_KEYS,UFER_TYPE

def scrapp(content):
    types_dict=make_dictionary(UFER_KEYS,UFER_TYPE)
    ufer_values = []
    for key in UFER_KEYS:
        id_case=('id="' + str(key)+'">')
        content_pos = content.find(id_case)
        start_pos = content.find(">",content_pos)
        if types_dict.get(key) != list:
            end_pos=content.find("<",start_pos+1)
            ufer_values.append(int_detector(content[start_pos+1:end_pos]))
        elif types_dict.get(key) == list:
            end_pos=content.find("</ul",start_pos+1)
            ufer_values.append(string_to_list(content[start_pos+1:end_pos]))
    return ufer_values
