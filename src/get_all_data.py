from os import PRIO_PROCESS
from get_values import get_name,get_description,get_driver,get_passengers,get_privacy,get_seats,get_propulsion,get_top_speed,get_price

from web_crawler import get_page,crawl_web

def get_all_values(content):

    name=get_name(content)
    desc=get_description(content)
    driver=get_driver(content)
    passengers=get_passengers(content)
    privacy=get_privacy(content)
    seats=get_seats(content)
    propulsion=get_propulsion(content)
    top_speed=get_top_speed(content)
    price=get_price(content)

    all=name,desc,driver,passengers,privacy,seats,propulsion,top_speed,price

    return(all)



links=crawl_web("https://charlos16v.github.io/proyecto-ufer/",3)
print(links)

#for i in links:
#    print(get_all_values(get_page(i)))


