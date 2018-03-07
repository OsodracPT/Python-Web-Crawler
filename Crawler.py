import requests
from bs4 import BeautifulSoup

def techSpider(maxPages):
    page = 1
    while page <= maxPages:
        url = "https://www.olx.pt/tecnologia-e-informatica/?search%5Bdescription%5D=1&page=" + str(page)
        source_code = requests.get(url)
        plainText = source_code.text
        soup = BeautifulSoup(plainText)
        for link in soup.findAll("a", {"class": "marginright5 link linkWithHash detailsLink"}):
            href = "https://www.olx.pt/anuncio" + link.get("href")
            #print(href)
            getSingleItemData(href)
        page +=1

def getSingleItemData(itemUrl):
    source_code = requests.get(itemUrl)
    plainText = source_code.text
    soup = BeautifulSoup(plainText)
    for itemName in soup.findAll("a", {"class" : "item-name"}):
        print(itemName.string)

techSpider(1)