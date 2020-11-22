def repair_link(link):
    if link.find("http://") not in link:
        link="http://"+link
        return link
    return link



a=urllib2.urlopen("http://google.com")
print a.getcode() # prints 200

if __name__ == "__main__":
    assert repair_link("./master.html") == "http://master.html"