from src.services.config.ufer_conf import UFER_KEYS
from src.services.scrapper.scrapp import scrapp
from src.services.crawler.get_content import get_content
import pytest


@pytest.mark.scrapp
# Casos de ejemplo se prueban con las constantes de configuración.
UFER_KEYS= ["price","name","description","amenities"]
UFER_TYPE= [int,str,str,list]

def test_scrapp():
    assert scrapp(get_content("https://charlos16v.github.io/proyecto-ufer/products/ufer_life.html")) == [15,"Ufer Lite","Ufer Life offers a low cost service for transport situations in the city, you will share space with other living beings in exchange for a cost, the service runs through a line of stops, instead of going to the different destinations of each client.",["Mask"]]
