from src.services.crawler.get_content import get_content

@pytest.mark.get_content
def test_get_content():
    assert get_content("https://charlos16v.github.io/proyecto-ufer/test.html") == "<body>        <ul id="extras">            <li>WiFi</li>            <li>Bluetooth</li>            <li>Tinted Screens</li>            <li>HiFi Audio System</li>            <li>A/C</li>            <li>Champagne Bottle</li>            <li>Water</li>            <li>Snacks</li>        </ul>        <h3 class="gold" id="nombre">Ufer Gold</h3>        <p>Driver: <span id="piloto">Autopilot</span></p>        <p>Passengers: <span id="pasajeros">1</span></p>        <p>Propulsion System: <span id="propulsion">Photon Engine</span></p>        <p>Speed (Km/h): <span id="velocidad-maxima">1080000000</span></p>        <p>Price (¢/min): <span id="precio">120</span></p>          <p>Privacy: <span id="privacidad">Private</span></p>        <h4 id="descripcion">Ufer Gold offers the most luxury experience in the entire galaxy. Includes all the features and amenities you can imagine.</h4>        <p>Seats: <span id="asientos">King Size</span></p>    </body></html>"
    #assert get_content("test")


#print(get_content("https://charlos16v.github.io/proyecto-ufer/test.html"))