# http://127.0.0.1:5500/ufer/index.html


def repair_link(link):
    if link.find("http://") == -1:
        link="http://127.0.0.1:5500/ufer/"+link
        return link
    return link





if __name__ == "__main__":
    assert repair_link("index.html") == "http://127.0.0.1:5500/ufer/index.html"
