# EN OBRAS
#from web_crawler import crawl_web,get_page


from typing import Counter


content=' <img src="./img/gold.svg" alt="Ufer Gold"> <div class="content"> <h3 id="name">Ufer Gold</h3> <h4 id="description">Ufer Gold offers the most luxury experience in the entire galaxy. Includes all the features and amenities you can imagine.</h4>'
def get_name(content):
    content_pos=content.find('id="name">')
    start_pos=content.find(">",content_pos)
    end_pos=content.find("<",start_pos+1)
    name_content=str(content[start_pos+1:end_pos])
    return name_content

if __name__ == '__main__':
    assert get_name(' <img src="./img/gold.svg" alt="Ufer Gold"> <div class="content"> <h3 id="name">Ufer Gold</h3> <h4 id="description">Ufer Gold offers the most luxury experience in the entire galaxy. Includes all the features and amenities you can imagine.</h4>') == "Ufer Gold"
    print("pass")


def get_description(content):
    content_pos=content.find('id="description">')
    start_pos=content.find(">",content_pos)
    end_pos=content.find("<",start_pos+1)
    desc_content=str(content[start_pos+1:end_pos])
    return desc_content

if __name__ == '__main__':
    assert get_description(' <img src="./img/gold.svg" alt="Ufer Gold"> <div class="content"> <h3 id="name">Ufer Gold</h3> <h4 id="description">Ufer Gold offers the most luxury experience in the entire galaxy. Includes all the features and amenities you can imagine.</h4>') == "Ufer Gold offers the most luxury experience in the entire galaxy. Includes all the features and amenities you can imagine."
    print("pass")


def get_driver(content):
    content_pos=content.find('id="driver">')
    start_pos=content.find(">",content_pos)
    end_pos=content.find("<",start_pos+1)
    driver_content=str(content[start_pos+1:end_pos])
    return driver_content

if __name__ == '__main__':
    assert get_driver('<section class="product gold"><img src="./img/gold.svg" alt="Uber Gold"><div class="content"><h3 id="name">Ufer Gold</h3><h4 id="description">Ufer Gold offers the most luxury experience in the entire galaxy. Includes all the features and amenities you can imagine.</h4><div class="features"><p>Driver: <span id="driver">Autopilot</span></p><p>Passengers: <span id="passengers">1</span></p><p>Privacy: <span id="privacy">Private</span></p><p>Seats: <span id="seats">King Size</span></p><p>Propulsion System: <span id="propulsion">Photon Engine</span></p><p>Speed (Km/h): <span id="top_speed">1080000000</span></p><p>Price (¢/min): <span id="price">120</span></p><h5>Amenities:</h4><ul id="amenities"><li>WiFi</li><li>Bluetooth</li><li>Tinted Screens</li><li>HiFi Audio System</li><li>A/C</li><li>Champagne Bottle</li><li>Water</li><li>Snacks</li></ul> </div> </div> </section>') == "Autopilot"
    print("pass auto")


def get_passengers(content):
    content_pos=content.find('id="passengers">')
    start_pos=content.find(">",content_pos)
    end_pos=content.find("<",start_pos+1)
    passengers_content=int(content[start_pos+1:end_pos])
    return passengers_content

if __name__ == '__main__':
    assert get_passengers('<section class="product gold"><img src="./img/gold.svg" alt="Uber Gold"><div class="content"><h3 id="name">Ufer Gold</h3><h4 id="description">Ufer Gold offers the most luxury experience in the entire galaxy. Includes all the features and amenities you can imagine.</h4><div class="features"><p>Driver: <span id="driver">Autopilot</span></p><p>Passengers: <span id="passengers">1</span></p><p>Privacy: <span id="privacy">Private</span></p><p>Seats: <span id="seats">King Size</span></p><p>Propulsion System: <span id="propulsion">Photon Engine</span></p><p>Speed (Km/h): <span id="top_speed">1080000000</span></p><p>Price (¢/min): <span id="price">120</span></p><h5>Amenities:</h4><ul id="amenities"><li>WiFi</li><li>Bluetooth</li><li>Tinted Screens</li><li>HiFi Audio System</li><li>A/C</li><li>Champagne Bottle</li><li>Water</li><li>Snacks</li></ul> </div> </div> </section>') == 1
    print("pass")


def get_privacy(content):
    content_pos=content.find('id="privacy">')
    start_pos=content.find(">",content_pos)
    end_pos=content.find("<",start_pos+1)
    privacy_content=str(content[start_pos+1:end_pos])
    return privacy_content

if __name__ == '__main__':
    assert get_privacy('<section class="product gold"><img src="./img/gold.svg" alt="Uber Gold"><div class="content"><h3 id="name">Ufer Gold</h3><h4 id="description">Ufer Gold offers the most luxury experience in the entire galaxy. Includes all the features and amenities you can imagine.</h4><div class="features"><p>Driver: <span id="driver">Autopilot</span></p><p>Passengers: <span id="passengers">1</span></p><p>Privacy: <span id="privacy">Private</span></p><p>Seats: <span id="seats">King Size</span></p><p>Propulsion System: <span id="propulsion">Photon Engine</span></p><p>Speed (Km/h): <span id="top_speed">1080000000</span></p><p>Price (¢/min): <span id="price">120</span></p><h5>Amenities:</h4><ul id="amenities"><li>WiFi</li><li>Bluetooth</li><li>Tinted Screens</li><li>HiFi Audio System</li><li>A/C</li><li>Champagne Bottle</li><li>Water</li><li>Snacks</li></ul> </div> </div> </section>') == "Private"
    print("pass")


def get_seats(content):
    content_pos=content.find('id="seats">')
    start_pos=content.find(">",content_pos)
    end_pos=content.find("<",start_pos+1)
    seats_content=str(content[start_pos+1:end_pos])
    return seats_content

if __name__ == '__main__':
    assert get_seats('<section class="product gold"><img src="./img/gold.svg" alt="Uber Gold"><div class="content"><h3 id="name">Ufer Gold</h3><h4 id="description">Ufer Gold offers the most luxury experience in the entire galaxy. Includes all the features and amenities you can imagine.</h4><div class="features"><p>Driver: <span id="driver">Autopilot</span></p><p>Passengers: <span id="passengers">1</span></p><p>Privacy: <span id="privacy">Private</span></p><p>Seats: <span id="seats">King Size</span></p><p>Propulsion System: <span id="propulsion">Photon Engine</span></p><p>Speed (Km/h): <span id="top_speed">1080000000</span></p><p>Price (¢/min): <span id="price">120</span></p><h5>Amenities:</h4><ul id="amenities"><li>WiFi</li><li>Bluetooth</li><li>Tinted Screens</li><li>HiFi Audio System</li><li>A/C</li><li>Champagne Bottle</li><li>Water</li><li>Snacks</li></ul> </div> </div> </section>') == "King Size"
    print("pass")


def get_propulsion(content):
    content_pos=content.find('id="propulsion">')
    start_pos=content.find(">",content_pos)
    end_pos=content.find("<",start_pos+1)
    propulsion_content=str(content[start_pos+1:end_pos])
    return propulsion_content

if __name__ == '__main__':
    assert get_propulsion('<section class="product gold"><img src="./img/gold.svg" alt="Uber Gold"><div class="content"><h3 id="name">Ufer Gold</h3><h4 id="description">Ufer Gold offers the most luxury experience in the entire galaxy. Includes all the features and amenities you can imagine.</h4><div class="features"><p>Driver: <span id="driver">Autopilot</span></p><p>Passengers: <span id="passengers">1</span></p><p>Privacy: <span id="privacy">Private</span></p><p>Seats: <span id="seats">King Size</span></p><p>Propulsion System: <span id="propulsion">Photon Engine</span></p><p>Speed (Km/h): <span id="top_speed">1080000000</span></p><p>Price (¢/min): <span id="price">120</span></p><h5>Amenities:</h4><ul id="amenities"><li>WiFi</li><li>Bluetooth</li><li>Tinted Screens</li><li>HiFi Audio System</li><li>A/C</li><li>Champagne Bottle</li><li>Water</li><li>Snacks</li></ul> </div> </div> </section>') == "Photon Engine"
    print("pass")


def get_top_speed(content):
    content_pos=content.find('id="top_speed">')
    start_pos=content.find(">",content_pos)
    end_pos=content.find("<",start_pos+1)
    top_speed_content=int(content[start_pos+1:end_pos])
    return top_speed_content

if __name__ == '__main__':
    assert get_top_speed('<section class="product gold"><img src="./img/gold.svg" alt="Uber Gold"><div class="content"><h3 id="name">Ufer Gold</h3><h4 id="description">Ufer Gold offers the most luxury experience in the entire galaxy. Includes all the features and amenities you can imagine.</h4><div class="features"><p>Driver: <span id="driver">Autopilot</span></p><p>Passengers: <span id="passengers">1</span></p><p>Privacy: <span id="privacy">Private</span></p><p>Seats: <span id="seats">King Size</span></p><p>Propulsion System: <span id="propulsion">Photon Engine</span></p><p>Speed (Km/h): <span id="top_speed">1080000000</span></p><p>Price (¢/min): <span id="price">120</span></p><h5>Amenities:</h4><ul id="amenities"><li>WiFi</li><li>Bluetooth</li><li>Tinted Screens</li><li>HiFi Audio System</li><li>A/C</li><li>Champagne Bottle</li><li>Water</li><li>Snacks</li></ul> </div> </div> </section>') == 1080000000
    print("pass")


def get_price(content):
    content_pos=content.find('id="price">')
    start_pos=content.find(">",content_pos)
    end_pos=content.find("<",start_pos+1)
    price_content=int(content[start_pos+1:end_pos])
    return price_content

if __name__ == '__main__':
    assert get_price('<section class="product gold"><img src="./img/gold.svg" alt="Uber Gold"><div class="content"><h3 id="name">Ufer Gold</h3><h4 id="description">Ufer Gold offers the most luxury experience in the entire galaxy. Includes all the features and amenities you can imagine.</h4><div class="features"><p>Driver: <span id="driver">Autopilot</span></p><p>Passengers: <span id="passengers">1</span></p><p>Privacy: <span id="privacy">Private</span></p><p>Seats: <span id="seats">King Size</span></p><p>Propulsion System: <span id="propulsion">Photon Engine</span></p><p>Speed (Km/h): <span id="top_speed">1080000000</span></p><p>Price (¢/min): <span id="price">120</span></p><h5>Amenities:</h4><ul id="amenities"><li>WiFi</li><li>Bluetooth</li><li>Tinted Screens</li><li>HiFi Audio System</li><li>A/C</li><li>Champagne Bottle</li><li>Water</li><li>Snacks</li></ul> </div> </div> </section>') == 120
    print("pass")





content='<section class="product gold"><img src="./img/gold.svg" alt="Uber Gold"><div class="content"><h3 id="name">Ufer Gold</h3><h4 id="description">Ufer Gold offers the most luxury experience in the entire galaxy. Includes all the features and amenities you can imagine.</h4><div class="features"><p>Driver: <span id="driver">Autopilot</span></p><p>Passengers: <span id="passengers">1</span></p><p>Privacy: <span id="privacy">Private</span></p><p>Seats: <span id="seats">King Size</span></p><p>Propulsion System: <span id="propulsion">Photon Engine</span></p><p>Speed (Km/h): <span id="top_speed">1080000000</span></p><p>Price (¢/min): <span id="price">120</span></p><h5>Amenities:</h4><ul id="amenities"><li>WiFi</li><li>Bluetooth</li><li>Tinted Screens</li><li>HiFi Audio System</li><li>A/C</li><li>Champagne Bottle</li><li>Water</li><li>Snacks</li></ul> </div> </div> </section>'
def get_amenities(content):

    content_pos=content.find('id="amenities">')
    start_pos=content.find(">",content_pos)
    end_pos=content.find("</ul",start_pos+1)
    amenities_content=str(content[start_pos+1:end_pos])

    amens=[]
    li_pos=0

    for e in amenities_content:
        if e == ">":
            start_list_pos=amenities_content.find(e,li_pos)
            end_list_pos=amenities_content.find("</li",li_pos)
            amens.append(str(amenities_content[start_list_pos+1:end_list_pos]))
            li_pos=end_list_pos+5

    return amens

print(get_amenities(content))

#if __name__ == '__main__':
#    assert get_amenities('<section class="product gold"><img src="./img/gold.svg" alt="Uber Gold"><div class="content"><h3 id="name">Ufer Gold</h3><h4 id="description">Ufer Gold offers the most luxury experience in the entire galaxy. Includes all the features and amenities you can imagine.</h4><div class="features"><p>Driver: <span id="driver">Autopilot</span></p><p>Passengers: <span id="passengers">1</span></p><p>Privacy: <span id="privacy">Private</span></p><p>Seats: <span id="seats">King Size</span></p><p>Propulsion System: <span id="propulsion">Photon Engine</span></p><p>Speed (Km/h): <span id="top_speed">1080000000</span></p><p>Price (¢/min): <span id="price">120</span></p><h5>Amenities:</h4><ul id="amenities"><li>WiFi</li><li>Bluetooth</li><li>Tinted Screens</li><li>HiFi Audio System</li><li>A/C</li><li>Champagne Bottle</li><li>Water</li><li>Snacks</li></ul> </div> </div> </section>') == ["WiFi", "Bluetooth", "Tinted Screens", "HiFi Audio System", "A/C", "Champagne Bottle", "Water", "Snacks"]
#    print("pass")







