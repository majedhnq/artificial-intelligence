import requests
url = "https://www.python.org/"
html = requests.get(url)
print(html.text)