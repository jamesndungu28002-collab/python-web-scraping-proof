import csv
import requests
from bs4 import BeautifulSoup

url=('https://books.toscrape.com')
response=requests.get(url).text
soup=BeautifulSoup(response, 'html.parser')

products=[]

for item in soup.find_all('article', class_='product_pod'):
    name=item.h3.a['title']
    price=item.find('p', class_='price_color').text

    product = {'Name':name, 'Price':price}
    products.append(product)

with open('books.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer =csv.DictWriter(file, fieldnames=['Name', 'Price'])
    writer.writeheader()
    writer.writerows(products)

print(f"Done! Saved {len(products)} books to books.csv")




