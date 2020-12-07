from src.services.scrapper.string_to_list import string_to_list
import pytest

@pytest.mark.string_to_list
def test_string_to_list():
    assert string_to_list('<li>WiFi</li><li>Mask</li></ul>') == ['WiFi', 'Mask']
    assert string_to_list('<li></li><li></li>') == ['','']
    assert string_to_list('<ul><li>WiFi</li><li>Mask</li></ul>') == ['<li>WiFi', 'Mask']
    assert string_to_list('<li>WiFi</li><li>Bluetooth</li><li>Tinted Screens</li><li>HiFi Audio System</li><li>A/C</li>'
                          '<li>Champagne Bottle</li><li>Water</li><li>Snacks</li>') == ['WiFi', 'Bluetooth', 'Tinted Screens', 'HiFi Audio System', 'A/C', 'Champagne Bottle', 'Water', 'Snacks']
