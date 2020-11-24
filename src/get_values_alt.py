from web_crawler import crawl_web,get_page


#content = '<section class="product gold"><img src="./img/gold.svg" alt="Uber Gold"><div class="content"><h3 id="name">Ufer Gold</h3><h4 id="description">Ufer Gold offers the most luxury experience in the entire galaxy. Includes all the features and amenities you can imagine.</h4><div class="features"><p>Driver: <span id="driver">Autopilot</span></p><p>Passengers: <span id="passengers">1</span></p><p>Privacy: <span id="privacy">Private</span></p><p>Seats: <span id="seats">King Size</span></p><p>Propulsion System: <span id="propulsion">Photon Engine</span></p><p>Speed (Km/h): <span id="top_speed">1080000000</span></p><p>Price (¢/min): <span id="price">120</span></p><h5>Amenities:</h4><ul id="amenities"><li>WiFi</li><li>Bluetooth</li><li>Tinted Screens</li><li>HiFi Audio System</li><li>A/C</li><li>Champagne Bottle</li><li>Water</li><li>Snacks</li></ul> </div> </div>'

ufer_keys = ['name', 'description', 'driver', 'passengers', 'privacy', 'seats', 'propulsion', 'top_speed', 'price']

def get_values(content):
    ufer_values = []
    for key in ufer_keys:
        id_case=('id="' + str(key)+'">')
        content_pos = content.find(id_case)
        start_pos = content.find(">",content_pos)
        end_pos=content.find("<",start_pos+1)
        ufer_values.append(content[start_pos+1:end_pos])
    return ufer_values

#if __name__ == '__main__':
#    assert get_values('<section class="product gold"><img src="./img/gold.svg" alt="Uber Gold"><div class="content"><h3 id="name">Ufer Gold</h3><h4 id="description">Ufer Gold offers the most luxury experience in the entire galaxy. Includes all the features and amenities you can imagine.</h4><div class="features"><p>Driver: <span id="driver">Autopilot</span></p><p>Passengers: <span id="passengers">1</span></p><p>Privacy: <span id="privacy">Private</span></p><p>Seats: <span id="seats">King Size</span></p><p>Propulsion System: <span id="propulsion">Photon Engine</span></p><p>Speed (Km/h): <span id="top_speed">1080000000</span></p><p>Price (¢/min): <span id="price">120</span></p><h5>Amenities:</h4><ul id="amenities"><li>WiFi</li><li>Bluetooth</li><li>Tinted Screens</li><li>HiFi Audio System</li><li>A/C</li><li>Champagne Bottle</li><li>Water</li><li>Snacks</li></ul> </div> </div>') == ['Ufer Gold', 'Ufer Gold offers the most luxury experience in the entire galaxy. Includes all the features and amenities you can imagine.', 'Autopilot', '1', 'Private', 'King Size', 'Photon Engine', '1080000000', '120']


links=crawl_web("https://charlos16v.github.io/proyecto-ufer/",3)
datos=[]
for i in links:
    putero.append((get_values(get_page(i))))
print(datos)
#print(putero)


