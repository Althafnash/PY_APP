import requests
from bs4 import BeautifulSoup

def Scrapper():
    url = input("Enter URL:: ")
    print("Just type an HTML tag you want to extract ")
    print("Eg::p")
    Tag = input("What do you want to extract :: ")

    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content , 'lxml')
    headlines = soup.find_all(Tag)

    for headline in headlines:
        print(headline.text)