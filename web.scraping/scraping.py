import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:
        text = quote.find("span", class_="text").text
        print(text)

        author = quote.find('small', class_='author').text
        print(f'Цитата: {text}')
        print(f'Автор: {author}')
        print('----------------------')
        # print(quote)