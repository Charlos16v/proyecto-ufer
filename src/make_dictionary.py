from get_values import UFER_KEYS,get_values
from get_content import get_content

def make_dictionary(a, b):
    return dict(zip(a, b))


print(make_dictionary(UFER_KEYS, get_values(get_content("https://charlos16v.github.io/proyecto-ufer/ufer_bus.html"))))