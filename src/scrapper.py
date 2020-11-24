# EN OBRAS
#from web_crawler import crawl_web,get_page


content=' <img src="./img/gold.svg" alt="Ufer Gold"> <div class="content"> <h3 id="name">Ufer Gold</h3> <h4 id="description">Ufer Gold offers the most luxury experience in the entire galaxy. Includes all the features and amenities you can imagine.</h4>'
def get_name(content):
    name_pos=content.find('id="name">')
    start_pos=content.find(">",name_pos)
    end_pos=content.find("<",start_pos+1)
    name_content=str(content[start_pos+1:end_pos])
    return name_content


if __name__ == '__main__':
    assert get_name(' <img src="./img/gold.svg" alt="Ufer Gold"> <div class="content"> <h3 id="name">Ufer Gold</h3> <h4 id="description">Ufer Gold offers the most luxury experience in the entire galaxy. Includes all the features and amenities you can imagine.</h4>') == "Ufer Gold"
    print("pass")




