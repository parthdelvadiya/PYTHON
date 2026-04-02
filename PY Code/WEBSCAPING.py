import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

titles = soup.find_all("h1")

for t in titles:
    print(t.text)