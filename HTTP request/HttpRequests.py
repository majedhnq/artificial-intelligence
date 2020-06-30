import requests
url = "http://google.com"
html = requests.get(url)
print(html.text)
file = open("C:\\Users\\Majed\\Desktop\\HTTP request\\url data.txt","w")
file.write(html.text)
file.close()