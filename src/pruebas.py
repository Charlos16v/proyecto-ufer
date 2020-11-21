from lxml import html
import requests

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)

# https://127.0.1.1:5000
# ../html/services.html
# ./index.html